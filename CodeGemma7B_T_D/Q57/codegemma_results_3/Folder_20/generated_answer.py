from itertools import combinations_with_replacement
        import numpy as np

def submatrix_with_particular_sum(matrix):
    iter_rows = combinations_with_replacement(range(matrix.shape[0]), 2)
    iter_cols = combinations_with_replacement(range(matrix.shape[1]), 2)
    list_with_possibilities = []
    for i in range(len(iter_rows)):
        for j in range(len(iter_cols)):
            list_with_possibilities.append(matrix[iter_rows[i][0]:iter_rows[i][1] + 1, iter_cols[j][0]:iter_cols[j][1] + 1])
    my_result = []
    for submatrix in list_with_possibilities:
        if np.sum(submatrix) == -57:
            if submatrix.tolist() not in my_result:
                my_result.append(submatrix.tolist())
    return my_result