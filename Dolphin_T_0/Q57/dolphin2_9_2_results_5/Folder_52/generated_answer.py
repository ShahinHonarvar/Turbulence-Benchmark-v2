import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if sum(matrix[i:, j:]) == 100:
                submatrices.append(matrix[i:, j:])
            if sum(matrix[:i, :j]) == 100:
                submatrices.append(matrix[:i, :j])
            if sum(matrix[i:, j:]) == 100:
                submatrices.append(matrix[i:, j:])
            if sum(matrix[i:, :j]) == 100:
                submatrices.append(matrix[i:, :j])
            if matrix.shape[0] - i >= 2 and matrix.shape[1] - j >= 2:
                if matrix[i, j] + matrix[i, j + 1] + matrix[i + 1, j] + matrix[i + 1, j + 1] == 100:
                    submatrices.append(matrix[i:i + 2, j:j + 2])
            if matrix.shape[0] - i >= 1 and matrix.shape[1] - j >= 3:
                if matrix[i, j] + matrix[i, j + 1] + matrix[i, j + 2] + matrix[i + 1, j] + matrix[i + 1, j + 1] + matrix[i + 1, j + 2] == 100:
                    submatrices.append(matrix[i:i + 2, j:j + 3])
            if matrix.shape[0] - i >= 3 and matrix.shape[1] - j >= 1:
                if matrix[i, j] + matrix[i + 1, j] + matrix[i + 2, j] + matrix[i, j + 1] + matrix[i + 1, j + 1] + matrix[i + 2, j + 1] == 100:
                    submatrices.append(matrix[i:i + 3, j:j + 2])
            if matrix.shape[0] - i >= 3 and matrix.shape[1] - j >= 3:
                if matrix[i, j] + matrix[i, j + 1] + matrix[i, j + 2] + matrix[i + 1, j] + matrix[i + 1, j + 1] + matrix[i + 1, j + 2] + matrix[i + 2, j] + matrix[i + 2, j + 1] + matrix[i + 2, j + 2] == 100:
                    submatrices.append(matrix[i:i + 3, j:j + 3])
    return submatrices