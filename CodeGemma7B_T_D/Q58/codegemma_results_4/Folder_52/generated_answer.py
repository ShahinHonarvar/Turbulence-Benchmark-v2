from itertools import combinations_with_replacement as cwr

def submatrix_with_n_numbers(matrix):
    N = len(matrix)
    count = 0
    for row1, row2 in cwr(range(N), 2):
        for col1, col2 in cwr(range(N), 2):
            submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
            if np.count_nonzero(submatrix == 147) == 147:
                count += 1
    return count