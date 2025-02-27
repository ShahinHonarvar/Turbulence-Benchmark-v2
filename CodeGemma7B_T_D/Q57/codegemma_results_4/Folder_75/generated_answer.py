import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_pairs = {}
    result = []
    for p1 in range(matrix.shape[0]):
        for p2 in range(matrix.shape[0]):
            col_sums = {}
            for p3 in range(p1, p2 + 1):
                for p4 in range(matrix.shape[1]):
                    col_sums.setdefault(p4, 0)
                    col_sums[p4] += matrix[p3, p4]
            for col_sums_value in col_sums.values():
                if 16 - col_sums_value in sum_pairs:
                    result.append(sum_pairs[16 - col_sums_value])
                else:
                    sum_pairs.setdefault(col_sums_value, [])
                    sum_pairs[col_sums_value].append((p1, p2))
    return result