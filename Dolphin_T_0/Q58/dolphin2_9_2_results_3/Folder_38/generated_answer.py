import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    array_size = len(matrix[0])
    matrix_size = len(matrix)
    for i in range(matrix_size):
        for j in range(array_size):
            if i + 1 < matrix_size and j + 2 < array_size:
                subarray = matrix[i:i + 2, j:j + 3]
                if len(subarray) == 3 and len(subarray[0]) == 3 and (len(set(subarray.flatten())) == 34):
                    count += 1
    return count