import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(matrix, target_sum):
        rows, cols = matrix.shape
        results = []
        for top in range(rows):
            temp_sum = np.zeros(cols, dtype=int)
            for bottom in range(top, rows):
                temp_sum += matrix[bottom]
                current_sum_map = {0: [-1]}
                current_sum = 0
                for right, value in enumerate(temp_sum):
                    current_sum += value
                    if current_sum - target_sum in current_sum_map:
                        for left in current_sum_map[current_sum - target_sum]:
                            submatrix = matrix[top:bottom + 1, left + 1:right + 1]
                            results.append(submatrix.tolist())
                    if current_sum not in current_sum_map:
                        current_sum_map[current_sum] = []
                    current_sum_map[current_sum].append(right)
        return results
    return find_submatrices_with_sum(matrix, -811)