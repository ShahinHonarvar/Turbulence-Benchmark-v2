import numpy as np

def submatrix_with_particular_sum(matrix):
    required_sum = 382
    result = []
    max_row = matrix.shape[0]
    max_col = matrix.shape[1]
    for start_row in range(max_row):
        for end_row in range(start_row, max_row):
            for start_col in range(max_col):
                for end_col in range(start_col, max_col):
                    temp_matrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    temp_sum = temp_matrix.sum()
                    if temp_sum == required_sum:
                        formatted_matrix = np.array(temp_matrix).tolist()
                        if formatted_matrix not in result:
                            result.append(formatted_matrix)
    return result