def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 75):
        for j in range(len(matrix) - 75):
            l = matrix[i:i + 76, j:j + 76]
            if np.all(l == 76):
                count += 1
    return count