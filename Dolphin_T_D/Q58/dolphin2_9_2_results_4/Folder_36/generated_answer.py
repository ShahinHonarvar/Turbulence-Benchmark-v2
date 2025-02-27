import numpy as np

def submatrix_with_n_numbers(matrix):
    array = np.array(matrix)
    count = 0
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            for m in range(i, array.shape[0]):
                for n in range(j, array.shape[1]):
                    subarray = array[i:m + 1, j:n + 1]
                    if len(subarray.flatten()) == 131:
                        count += 1
    if count > 0:
        return count
    else:
        return 0