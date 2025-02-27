from typing import List

def submatrix_with_particular_sum(matrix):
    """
    """
    if not matrix:
        return []
    row, col = matrix.shape
    result = []
    for i in range(row):
        for j in range(col):
            for ii in range(i, row):
                for jj in range(j, col):
                    submatrix = matrix[i:ii + 1, j:jj + 1]
                    sum_submatrix = sum(sum(submatrix))
                    if sum_submatrix == 84:
                        result.append(submatrix)
    return result