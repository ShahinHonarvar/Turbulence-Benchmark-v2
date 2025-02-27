from numpy import where

def submatrix_with_n_numbers(matrix):
    w, h = matrix.shape
    count = 0
    for x in range(w):
        for y in range(h):
            for y2 in range(y, h):
                for x2 in range(x, w):
                    current_mat = matrix[y:y2 + 1, x:x2 + 1]
                    if set(map(len, current_mat.flatten())) == {29}:
                        count += 1
    return count