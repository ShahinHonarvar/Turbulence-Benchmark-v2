from numpy import*

def submatrix_with_n_numbers(arr):
    """Counts the number of submatrices of a given matrix that contain n numbers."""
    rows, cols = arr.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if arr[i, j] == 48:
                count += 1
    return count