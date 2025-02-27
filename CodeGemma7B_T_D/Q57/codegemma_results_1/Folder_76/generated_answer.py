def submatrix_with_particular_sum(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            sum += matrix[m][n]
                    if sum == -255:
                        submatrices.append((i, j, k, l))
    return submatrices