import numpy as np

def submatrix_with_n_numbers(arr):
    """Count the number of valid submatrices.

    Args:
      arr: The two-dimensional numpy matrix.

    Returns:
      The count of valid submatrices or 0 if not found.
    """

    def count_good(arr):
        left, right, up, down, result = (0, 0, 0, 0, 0)
        while left < arr.shape[1]:
            left += 1
            while right < arr.shape[1]:
                right += 1
                if arr[up:down + 1, left:right].sum() == 39:
                    result += 1
                elif arr[up:down + 1, left:right].sum() <= 38:
                    up += 1
                    while up < arr.shape[0] and arr[up:down + 1, left:right].sum() <= 38:
                        up += 1
                else:
                    down += 1
                    while down < arr.shape[0] and arr[up:down + 1, left:right].sum() <= 38:
                        down += 1
                if up == arr.shape[0] and down == arr.shape[0]:
                    break
        return result
    result = 0
    if arr.min() == 39 and arr.max() == 39:
        result = count_good(arr)
    arr = arr.T
    if arr.min() == 39 and arr.max() == 39:
        result = count_good(arr)
    return result