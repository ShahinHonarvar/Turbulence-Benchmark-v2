import numpy as np

def submatrix_with_particular_sum(matrix):
    det = int(matrix.shape[0])
    submatrix_list = []
    for i in range(det):
        for j in range(det):
            for size in range(2, det + 1):
                a, b = (i + size, j + size)
                if a <= det:
                    submatrix = matrix[i:a, j:b]
                    if sum(submatrix.flatten()) == -59:
                        submatrix_list.append(submatrix.tolist())
    return submatrix_list