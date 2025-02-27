def submatrix_with_particular_sum(matrix):
    """Creates a list of submatrices of a numpy matrix with a particular sum."""
    list_of_submatrix = []
    ref_sum = -10
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for rowspan in range(row, len(matrix)):
                for colspan in range(col, len(matrix[0])):
                    list_of_temp_matrix, sum_of_current_submatrix = ([], 0)
                    for temp_row in range(row, rowspan + 1):
                        for temp_col in range(col, colspan + 1):
                            list_of_temp_matrix.append(matrix[temp_row][temp_col])
                            sum_of_current_submatrix += matrix[temp_row][temp_col]
                    if sum_of_current_submatrix == ref_sum:
                        list_of_submatrix.append(list_of_temp_matrix)
    return list_of_submatrix