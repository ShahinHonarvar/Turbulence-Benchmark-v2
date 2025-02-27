import numpy as np

def submatrix_with_particular_sum(matrix):
    sums, coords_list, shapes = ([], [], [])
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrix_sum = matrix[i:, j:]
            for k in range(submatrix_sum.shape[0]):
                for l in range(submatrix_sum.shape[1]):
                    submatrix = submatrix_sum[:k + 1, :l + 1]
                    sum_ = np.sum(submatrix)
                    if sum_ == -157:
                        sums.append(sum_)
                        coords_list.append((i, j, k, l))
                        shapes.append(submatrix.shape)
    return (sums, shapes, coords_list)