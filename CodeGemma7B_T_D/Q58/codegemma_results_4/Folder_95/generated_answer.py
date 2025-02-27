import numpy as np

def submatrix_with_n_numbers(mat):
    """
    Count the number of submatrices with a given number of integers.
    
    Args:
    mat: A numpy matrix of integers.
    
    Returns:
    The number of submatrices with the given number of integers.
    """
    num_rows, num_cols = mat.shape
    count = 0
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i + 1, num_rows):
                for l in range(j + 1, num_cols):
                    submatrix = mat[i:k + 1, j:l + 1]
                    if np.sum(submatrix == 87) == 87:
                        count += 1
    return count