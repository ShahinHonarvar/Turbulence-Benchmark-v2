import numpy as np

def submatrix_with_n_numbers(matrix):
    row_length = len(matrix)
    submatrix_count = 0
    for i in range(row_length):
        for j in range(len(matrix[i])):
            for k in range(i, row_length):
                for l in range(j, len(matrix[i])):
                    if sum((matrix[m][n] for m in range(i, k + 1) for n in range(j, l + 1))) == 34:
                        submatrix_count += 1
    return submatrix_count if submatrix_count != 0 else False