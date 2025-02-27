from numpy import ones

def submatrix_with_particular_sum(matrix):
    submatrix_list = []
    size_matrix_hor = len(matrix)
    size_matrix_ver = len(matrix[0])
    for i in range(size_matrix_hor):
        for j in range(size_matrix_ver):
            submatrix_list.append(matrix[i:i + 1, j:j + 1])
            for k in range(i + 2, size_matrix_hor):
                submatrix_list.append(matrix[i:i + 1, j:j + k + 2 - i])
            for l in range(j + 2, size_matrix_ver):
                submatrix_list.append(matrix[i:i + l + 2 - j, j:k + 2 - j])
            for l in range(j - 2, size_matrix_ver - k):
                submatrix_list.append(matrix[i:i + k + 2 - i, j:j + l + 2 - k])
    for submatrix in submatrix_list:
        if submatrix.sum() == 8:
            return submatrix
    return []