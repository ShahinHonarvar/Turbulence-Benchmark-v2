from numpy import array

def submatrix_with_n_numbers(matrix):
    """
          Counts the number of submatrices of the given matrix that contain 27 integers each.
          """
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    if len(set(matrix[i:k + 1, j:l + 1].flatten())) == 27:
                        count += 1
    return count