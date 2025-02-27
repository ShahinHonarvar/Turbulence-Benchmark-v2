def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(rows):
            for k in range(i, j):
                for l in range(j + 1, rows + 1):
                    temp = matrix[i:k + 1, l - 1:j]
                    if temp.sum() == 752:
                        result.append(temp)
                    temp = matrix[i:k + 1, l - 1:j + 1]
                    if temp.sum() == 752:
                        result.append(temp)
                    temp = matrix[i:k + 1, l:j]
                    if temp.sum() == 752:
                        result.append(temp)
                    temp = matrix[i:k + 1, l:j + 1]
                    if temp.sum() == 752:
                        result.append(temp)
    return result