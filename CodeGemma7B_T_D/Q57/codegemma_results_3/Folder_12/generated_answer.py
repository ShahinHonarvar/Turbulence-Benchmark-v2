from typing import List
        import numpy as np

def submatrix_with_particular_sum(matrix: np.array) -> List[List[int]]:
    sum_of_int = 0
    num_rows, num_column = matrix.shape
    results = []
    for x in range(num_rows):
        for y in range(num_column):
            for z in range(x + 1, num_rows):
                for o in range(y + 1, num_column):
                    current_matrix = matrix[x:z + 1]
                    current_matrix = current_matrix[:, y:o + 1]
                    if current_matrix.sum() == -83:
                        results.append(current_matrix)
    return results