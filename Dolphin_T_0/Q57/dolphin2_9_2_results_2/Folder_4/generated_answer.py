import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[0])):
                    sliced_matrix = np.array(matrix[i:x + 1, j:y + 1])
                    slice_sum = np.sum(sliced_matrix)
                    if slice_sum == 87:
                        submatrices.append(sliced_matrix)
    return submatrices