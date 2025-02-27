def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for x in range(i + 1):
                for y in range(j + 1):
                    subset = matrix[x:i + 1, y:j + 1]
                    if len(subset[subset == 66]) == n:
                        count += 1
    return count