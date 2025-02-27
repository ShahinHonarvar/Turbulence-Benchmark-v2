from numpy import array

def submatrix_with_particular_sum(matrix: array) -> list:
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix)):
                    current_sum = matrix[i][j] + matrix[i][l] + matrix[k][j] + matrix[k][l]
                    if current_sum == 41:
                        result.append([matrix[i][j], matrix[i][l], matrix[k][j], matrix[k][l]])
    return result