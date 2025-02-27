import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrix_list = []
    dim1 = len(matrix)
    dim2 = len(matrix[0])
    for i in range(dim1):
        for j in range(dim2):
            for k in range(i + 1, dim1 + 1):
                for l in range(j + 1, dim2 + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -394:
                        submatrix_list.append(submatrix.tolist())
    return submatrix_list