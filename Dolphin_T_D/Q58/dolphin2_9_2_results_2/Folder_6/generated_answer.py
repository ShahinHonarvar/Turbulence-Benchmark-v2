import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    n = 122
    m_rows, m_cols = matrix.shape
    for i in range(m_rows):
        for j in range(m_cols):
            for k in range(i + 1, m_rows):
                for l in range(j + 1, m_cols):
                    s_matrix = matrix[i:k, j:l]
                    if s_matrix.size == n:
                        submatrix_count += 1
    return submatrix_count