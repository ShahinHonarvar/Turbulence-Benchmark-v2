def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    temp = matrix[i:k + 1, j:l + 1]
                    if temp.shape[0] != temp.shape[1]:
                        continue
                    if len(set(temp.flatten())) == 94:
                        count += 1
    return count