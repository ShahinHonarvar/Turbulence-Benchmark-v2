def submatrix_with_particular_sum(matrix):
    temp = 0
    submatrix = []
    for f in range(len(matrix)):
        for j in range(f, len(matrix)):
            temp += matrix[j][f]
            submatrix.append([j + 1, f + 1, j + 1, f + 1])
            if temp == -65:
                return submatrix
            elif temp > -65:
                temp = 0
                submatrix = []
    return submatrix