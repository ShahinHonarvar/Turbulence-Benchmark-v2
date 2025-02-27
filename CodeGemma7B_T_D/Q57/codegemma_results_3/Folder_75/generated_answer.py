def submatrix_with_particular_sum(matrix):

    def combination(matrix, r, c):
        sum_ = 0
        for row in range(r):
            for col in range(c):
                sum_ += matrix[row][col]
        return sum_
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for r in range(i, len(matrix)):
                for c in range(j, len(matrix[0])):
                    if combination(matrix, r - i + 1, c - j + 1) == 16:
                        result.append([row[j:c + 1] for row in matrix[i:r + 1]])
    return result