import numpy as np

def submatrix_with_particular_sum(arr):
    list_of_submatrices = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            for a in range(i, len(arr)):
                for b in range(j, len(arr)):
                    sum = 0
                    for c in range(i, a + 1):
                        for d in range(j, b + 1):
                            sum += arr[c][d]
                    if sum == 17:
                        list_of_submatrices.append(arr[i:a + 1, j:b + 1])
    return list_of_submatrices