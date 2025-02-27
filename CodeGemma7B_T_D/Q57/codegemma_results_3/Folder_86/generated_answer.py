def submatrix_with_particular_sum(matrix):
    start_row = 0
    start_column = 0
    end_row = len(matrix) - 1
    end_column = len(matrix[0]) - 1
    submatrix_list = []
    for r in range(start_row, end_row + 1):
        for c in range(start_column, end_column + 1):
            for i in range(r, end_row + 1):
                for j in range(c, end_column + 1):
                    submatrix = matrix[r:i + 1, c:j + 1]
                    if submatrix.sum() == -394:
                        submatrix_list.append(submatrix)
    return submatrix_list