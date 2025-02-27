import numpy as np

def submatrix_with_particular_sum(matrix):
    """
  This function takes one argument which is a two-dimensional numpy matrix of integers.
  The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 997.
  If no such submatrix is found, the function should return an empty list.
  """
    sum_of_all_rows = matrix.sum(axis=1).tolist()
    sum_of_all_cols = matrix.sum(axis=0).tolist()
    all_row_indices = list(range(len(sum_of_all_rows)))
    all_col_indices = list(range(len(sum_of_all_cols)))
    submatrices = []
    for row_index in all_row_indices:
        for col_index in all_col_indices:
            the_lower_row_index = row_index + 1
            the_upper_row_index = len(sum_of_all_rows) - 1
            the_lower_col_index = col_index + 1
            the_upper_col_index = len(sum_of_all_cols) - 1
            for r in all_row_indices[row_index:the_lower_row_index + 1]:
                for c in all_col_indices[col_index:the_lower_col_index + 1]:
                    the_upper_row_index = min(the_upper_row_index, r)
                    the_upper_col_index = min(the_upper_col_index, c)
                    the_lower_row_index = max(the_lower_row_index, r)
                    the_lower_col_index = max(the_lower_col_index, c)
                    if sum_of_all_rows[r] - sum_of_all_cols[c] == 997:
                        submatrix = matrix[r:the_lower_row_index + 1, c:the_lower_col_index + 1]
                        submatrices.append(submatrix)
    return submatrices if submatrices else []