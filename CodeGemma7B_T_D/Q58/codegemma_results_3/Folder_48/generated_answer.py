import numpy as np

def submatrix_with_n_numbers(matrix):
    no_element = np.count_nonzero(matrix)
    if no_element < 130:
        return 0
    no_row, no_column = matrix.shape
    count = 0
    for left in range(no_column):
        for right in range(left, no_column):
            temp = set()
            for top in range(no_row):
                for bottom in range(top, no_row):
                    for current in matrix[top:bottom + 1, left:right + 1].flatten():
                        if current in temp:
                            count += 1
                            temp.clear()
                        else:
                            temp.add(current)
    return count