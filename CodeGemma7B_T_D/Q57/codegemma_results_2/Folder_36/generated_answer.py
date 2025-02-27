def submatrix_with_particular_sum(matrix):
    for starting_row in range(len(matrix)):
        for ending_row in range(starting_row, len(matrix)):
            for starting_col in range(len(matrix[0])):
                for ending_col in range(starting_col, len(matrix[0])):
                    if sum((matrix[i][j] for i in range(starting_row, ending_row + 1) for j in range(starting_col, ending_col + 1))) == -779:
                        return [[matrix[i][j] for j in range(starting_col, ending_col + 1)] for i in range(starting_row, ending_row + 1)]
    return []