import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for start_row in range(m):
        for end_row in range(start_row, m):
            row_sum = np.zeros(n)
            for row in range(start_row, end_row + 1):
                row_sum += matrix[row]
                current_sum = 0
                sum_dict = {0: -1}
                for col in range(n):
                    current_sum += row_sum[col]
                    if current_sum - -157 in sum_dict:
                        start_col = sum_dict[current_sum - -157] + 1
                        end_col = col
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        submatrices.append(submatrix)
                    if current_sum not in sum_dict:
                        sum_dict[current_sum] = col
    return submatrices