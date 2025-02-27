def submatrix_with_n_numbers(matrix):
    """This function returns the count of all submatrices of the given
    matrix that contain 166 integers each. If no such
    submatrix is found, the function should return 0."""
    total_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 166:
                for a in range(i, len(matrix)):
                    for b in range(j, len(matrix)):
                        if matrix[a][b] == 166:
                            current_submatrix = [row[j:b + 1] for row in matrix[i:a + 1]]
                            if len(current_submatrix) == len(current_submatrix[0]) and len(current_submatrix) == 166:
                                total_count += 1
    return total_count