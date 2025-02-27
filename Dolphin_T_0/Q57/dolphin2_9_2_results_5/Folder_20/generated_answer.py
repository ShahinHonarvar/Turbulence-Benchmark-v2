import numpy as np

def submatrix_with_particular_sum(matrix):
    sums = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp = matrix[i:, j:]
            s = np.sum(temp)
            if s in sums:
                sums[s].append(temp)
            else:
                sums[s] = [temp]
    if -57 in sums:
        return sums[-57]
    else:
        return []