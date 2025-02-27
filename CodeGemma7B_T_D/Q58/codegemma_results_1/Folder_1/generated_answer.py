def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            candidate = set()
            for k in range(len(matrix[0])):
                candidate.add(matrix[i][k])
                candidate.add(matrix[j][k])
            if len(candidate) == 23:
                count += 1
    return count