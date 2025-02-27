def submatrix_with_n_numbers(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    submatrices.append(submatrix)
    count = 0
    for submatrix in submatrices:
        if sum(submatrix.flatten()) == 96:
            count += 1
    return count