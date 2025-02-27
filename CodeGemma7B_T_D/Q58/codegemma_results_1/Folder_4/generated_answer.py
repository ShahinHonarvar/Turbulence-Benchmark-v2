import numpy as np

def submatrix_with_n_numbers(mat):
    rows, cols = mat.shape
    count = 0
    for x in range(rows):
        for y in range(cols):
            for k in range(x, rows):
                for l in range(y, cols):
                    submatrix = [i[y:l + 1] for i in mat[x:k + 1]]
                    if len(submatrix) == len(set([item for sublist in submatrix for item in sublist])) == 15:
                        count += 1
    return count