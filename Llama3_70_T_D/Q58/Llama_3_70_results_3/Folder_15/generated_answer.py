import numpy as np
import itertools

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for submatrix_size in [(1, 2), (2, 1), (2, 2)]:
        for row in range(rows - submatrix_size[0] + 1):
            for col in range(cols - submatrix_size[1] + 1):
                submatrix = matrix[row:row + submatrix_size[0], col:col + submatrix_size[1]]
                if len(submatrix.flatten()) == 2:
                    count += 1
                elif len(submatrix.flatten()) > 2:
                    for r in range(submatrix_size[0]):
                        for c in range(submatrix_size[1]):
                            for r_offset in range(submatrix_size[0]):
                                for c_offset in range(submatrix_size[1]):
                                    if r != r_offset or c != c_offset:
                                        submatrix_sub = np.array([[submatrix[r, c], submatrix[r, c_offset]], [submatrix[r_offset, c], submatrix[r_offset, c_offset]]])
                                        if len(submatrix_sub.flatten()) == 2:
                                            count += 1
    return count