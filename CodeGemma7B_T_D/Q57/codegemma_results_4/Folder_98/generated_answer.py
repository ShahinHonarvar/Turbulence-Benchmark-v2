from typing import List
import numpy as np

def submatrix_with_particular_sum(arr):
    sum_dict = {}
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            for k in range(i, arr.shape[0]):
                for l in range(j, arr.shape[1]):
                    submatrix = arr[i:k + 1, j:l + 1]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum in sum_dict:
                        sum_dict[submatrix_sum].append((i, j, k, l))
                    else:
                        sum_dict[submatrix_sum] = [(i, j, k, l)]
    res = []
    for k, v in sum_dict.items():
        sums = [(0, 0)]
        for i, j, k, l in v:
            sums.append((i, j, k, l))
        result = get_result(sums)
        res.append(result) if result != [] else None
    return res

def get_result(sums):
    sums.sort()
    result = []
    for i in range(len(sums) - 1):
        for j in range(i + 1, len(sums)):
            submatrix_1 = sums[i]
            submatrix_2 = sums[j]
            if submatrix_1[3] + 1 == submatrix_2[1] and submatrix_1[2] + 1 == submatrix_2[0]:
                result.append((submatrix_1, submatrix_2))
    return result