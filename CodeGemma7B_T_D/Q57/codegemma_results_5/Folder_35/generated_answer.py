def submatrix_with_particular_sum(matrix):
    res = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            for i in range(r, len(matrix)):
                for j in range(c, len(matrix[0])):
                    sub_matrix = matrix[r:i + 1, c:j + 1]
                    if sum(sum(sub_matrix)) == 432:
                        res.append(sub_matrix)
    return res