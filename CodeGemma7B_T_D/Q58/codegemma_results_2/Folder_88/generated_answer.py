def submatrix_with_n_numbers(matrix):
    total_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp_matrix = np.array([[row[j:i + 1] for row in matrix[j:i + 1]]])
            if np.shape(temp_matrix) == (1, 1):
                temp_matrix = temp_matrix.flatten()
            if np.size(temp_matrix) == 67:
                total_count += 1
    return total_count