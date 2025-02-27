def submatrix_with_n_numbers(matrix):
    num_of_elements = 23
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - num_of_elements + 1):
        for j in range(cols - num_of_elements + 1):
            if np.count_nonzero(matrix[i:i + num_of_elements, j:j + num_of_elements]) == num_of_elements:
                count += 1
    return count