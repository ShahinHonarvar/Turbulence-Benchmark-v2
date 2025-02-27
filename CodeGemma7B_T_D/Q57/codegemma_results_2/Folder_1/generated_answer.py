from sklearn.decomposition import PCA
        import numpy as np
        import pandas as pd

def submatrix_with_particular_sum(matrix):
    list_submatrix = list()
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = np.array([row[l:l + (l - j + 1)] for row in matrix[i:k + 1]])
                    if np.sum(submatrix) == -25:
                        list_submatrix.append(submatrix)
                        count += 1
    if count == 0:
        return list_submatrix
    else:
        return list_submatrix