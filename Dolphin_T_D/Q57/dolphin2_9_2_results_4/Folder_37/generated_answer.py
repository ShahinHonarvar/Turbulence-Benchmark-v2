import numpy as np

def submatrix_with_particular_sum(matrix):
    indices = np.where(matrix == -82)
    xmin = indices[0].min()
    xmax = indices[0].max()
    ymin = indices[1].min()
    ymax = indices[1].max()
    submatrix = matrix[xmin:xmax + 1, ymin:ymax + 1]
    sum_submatrix = submatrix.sum()
    if sum_submatrix == -82:
        return [submatrix]
    else:
        return []