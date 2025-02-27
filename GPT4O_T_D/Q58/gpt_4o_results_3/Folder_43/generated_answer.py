import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(arr, target):
        rows, cols = arr.shape
        submat_count = 0
        for r1 in range(rows):
            for r2 in range(r1, rows):
                prefix_sum = np.zeros(cols)
                for c in range(cols):
                    for r in range(r1, r2 + 1):
                        prefix_sum[c] += arr[r][c]
                running_sum = 0
                sum_dict = {}
                sum_dict[0] = 1
                for val in prefix_sum:
                    running_sum += val
                    if running_sum - target in sum_dict:
                        submat_count += sum_dict[running_sum - target]
                    if running_sum in sum_dict:
                        sum_dict[running_sum] += 1
                    else:
                        sum_dict[running_sum] = 1
        return submat_count
    flat_len = matrix.size
    if flat_len < 85:
        return 0
    submatrices_count = 0
    rows, cols = matrix.shape
    for subrows in range(1, rows + 1):
        for subcols in range(1, cols + 1):
            if subrows * subcols == 85:
                submatrices_count += count_submatrices(matrix, 0)
    return submatrices_count