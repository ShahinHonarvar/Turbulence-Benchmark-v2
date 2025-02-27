import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    sum_arr, ans = (np.zeros((m, n + 1), dtype=int), [])
    for i in range(m):
        for j in range(n):
            sum_arr[i, j + 1] = sum_arr[i, j] + matrix[i, j]
    for j in range(1, n + 1):
        for _sum in range(m + 1):
            if sum_arr[:, j] == _sum:
                cur_ans = []
                for i in range(m):
                    cur_ans.append((i, sum_arr[i, j - 1], sum_arr[i, j]))
                    ans.append(cur_ans)
    for i in range(1, m + 1):
        for _sum in range(n + 1):
            if sum_arr[i - 1, :] == _sum:
                cur_ans = []
                for j in range(n):
                    cur_ans.append((sum_arr[i - 1, j + 1], sum_arr[i, j], j))
                    ans.append(cur_ans)
    return [sq if np.sum(matrix[sq[1][0]:sq[1][2] + 1, sq[2]:sq[2] + 1]) == 59 else [] for sq in ans]