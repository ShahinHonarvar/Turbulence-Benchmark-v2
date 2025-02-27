import numpy as np

def submatrix_with_n_numbers(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(i, len(arr)):
                for l in range(j, len(arr[0])):
                    matrix = arr[i:k + 1, j:l + 1]
                    if len(np.unique(matrix)) == 47:
                        count += 1
    return count