from numpy import matrix as npmatrix

def submatrix_with_n_numbers(matrix):
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            for width in range(len(matrix) - x):
                for height in range(len(matrix) - y):
                    submatrix = matrix[x:x + width + 1, y:y + height + 1]
                    if submatrix.size == 67 and submatrix.sum() == 67 * 33:
                        count += 1
    return count