def submatrix_with_particular_sum(matrix):
    ans = []
    for matrix_row in matrix:
        for matrix_col in matrix_row:
            temp_ans = []
            for row in matrix:
                temp = row[matrix_col:matrix_col + matrix_row[matrix_col]].tolist()
                temp_ans.append(temp)
            if sum(map(sum, temp_ans)) == 41:
                ans.append(temp_ans)
    return ans