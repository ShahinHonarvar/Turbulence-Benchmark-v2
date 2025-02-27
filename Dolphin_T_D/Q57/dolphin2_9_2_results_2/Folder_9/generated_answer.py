from typing import List
import numpy as np

def submatrix_with_particular_sum(matrix: np.array) -> List:
    row, col = matrix.shape
    submatrix = []
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    sub_array = matrix[i:k + 1, j:l + 1]
                    if sum(sub_array.flatten()) == -86 and sub_array.shape != matrix.shape:
                        submatrix.append(sub_array)
    return submatrix