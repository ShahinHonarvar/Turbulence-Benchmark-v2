import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 77:
                submatrices.append(np.array([[matrix[i][j]]]))
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if i != k or j != l:
                        submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                        if submatrix_sum == 77:
                            submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices if submatrices else []