import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    _sum = 0
    for r1 in range(len(matrix)):
        for r2 in range(r1, len(matrix)):
            _sum = 0
            for c1 in range(len(matrix[0])):
                for c2 in range(c1, len(matrix[0])):
                    for r in range(r1, r2 + 1):
                        for c in range(c1, c2 + 1):
                            _sum += matrix[r][c]
                    if _sum == -90:
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        results.append(submatrix.tolist())
    if not results:
        return []
    else:
        return results