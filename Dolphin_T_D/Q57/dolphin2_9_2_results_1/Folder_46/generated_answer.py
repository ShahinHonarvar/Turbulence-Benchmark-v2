import numpy as np

def submatrix_with_particular_sum(matrix):
    N = len(matrix)
    sums = {}
    submatrices = []
    for x1 in range(N):
        for x2 in range(x1, N):
            for y1 in range(N):
                for y2 in range(y1, N):
                    submatrix_sum = np.sum(matrix[x1:x2 + 1, y1:y2 + 1])
                    if submatrix_sum in sums:
                        sums[submatrix_sum].append([x1, x2, y1, y2])
                    else:
                        sums[submatrix_sum] = [[x1, x2, y1, y2]]
    if 416 in sums:
        for submatrix in sums[416]:
            submatrices.append([matrix[submatrix[0]:submatrix[1] + 1, submatrix[2]:submatrix[3] + 1]])
    return submatrices