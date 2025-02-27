import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 53
    result = 0
    for left in range(matrix.shape[0]):
        for right in range(left, matrix.shape[0]):
            for down in range(matrix.shape[1]):
                for up in range(down, matrix.shape[1]):
                    submatrix = matrix[left:right + 1, down:up + 1]
                    if submatrix.sum() == n * n:
                        count = 0
                        for row in submatrix:
                            for element in row:
                                if element == n:
                                    count += 1
                        if count == n:
                            result += 1
    return result