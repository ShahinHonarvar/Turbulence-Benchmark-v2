from scipy.signal import convolve2d

def submatrix_with_n_numbers(matrix):
    if matrix.shape[0] < 11 or matrix.shape[1] < 11 or (matrix < 0).any() or (matrix > 9).any():
        return 0
    kernel = [[1] * 11 for _ in range(11)]
    result = convolve2d(matrix, kernel, 'same')
    return (result == 131).sum()