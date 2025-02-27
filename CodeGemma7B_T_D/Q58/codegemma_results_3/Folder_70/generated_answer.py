def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 173:
                current_count = 0
                for k in range(i, rows):
                    for l in range(j, columns):
                        if matrix[k][l] == 173:
                            current_count += 1
                            if current_count == 173:
                                submatrix_count += 1
                            elif current_count > 173:
                                break
                if current_count == 173:
                    submatrix_count += 1
    return submatrix_count