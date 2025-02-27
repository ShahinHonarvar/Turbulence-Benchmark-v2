def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 51 and np.all(submatrix, axis=0).any() and np.all(submatrix, axis=1).any():
                        count += 1
    return count