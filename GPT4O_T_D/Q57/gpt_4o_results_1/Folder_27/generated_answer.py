import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    results = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
                    if submatrix_sum == 77:
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        results.append(submatrix.tolist())
    return results