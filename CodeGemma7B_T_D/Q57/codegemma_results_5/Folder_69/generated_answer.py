def submatrix_with_particular_sum(matrix):
    """
    Submatrix with particular sum
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    current_sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            current_sum += matrix[m][n]
                    if current_sum == 752:
                        return [[row[j:l + 1] for row in matrix[i:k + 1]]]
    return []