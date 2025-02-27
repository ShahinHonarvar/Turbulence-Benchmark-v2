def submatrix_with_n_numbers(matrix):
    result = 0
    temp = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 176:
                temp.clear()
                continue
            temp.add((i, j))
            if len(temp) == 176:
                result += 1
                temp.clear()
    return result