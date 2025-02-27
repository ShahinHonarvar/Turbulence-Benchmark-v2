import numpy as np

def submatrix_with_particular_sum(matrix):
    n_Axes = matrix.ndim
    sub_matrix = matrix.tolist()
    sum_sub_m = -20
    if n_Axes != 2:
        return 'Invalid matrix: Must be 2-D'
    if cond1 and cond3:
        sum_cond1_row = np.sum(matrix, 1)
        sum_cond2 = np.sum(matrix, 0)
        if min(sum_cond1_row) >= 0 and min(sum_cond2) >= 0:
            for thr in range(min(min(sum_cond1_row), min(sum_cond2)), -1, -1):
                if thr == sum_sub_m:
                    cond2 = True
                    cond3 = False
                else:
                    cond1 = False
    elif cond1 and cond2:
        n_Bxes = len(sub_matrix[0])
        for k in range(len(sub_matrix)):
            n_Axes_k = len(sub_matrix[k])
            list_a = []
            for z in range(n_Bxes - sum_sub_m + 1):
                list_a.append(matrix[k][z:z + sum_sub_m])
                list_b = []
            for y in range(sum_sub_m, n_Axes_k):
                list_b.append(matrix[k][z:y + 1])
                for x in range(len(list_a)):
                    for d in range(len(list_b[x])):
                        if list_a[x][0:sum_sub_m + d] in list_b[x]:
                            cond3 = True
                            return list_a[x][0:sum_sub_m + d]
    return []