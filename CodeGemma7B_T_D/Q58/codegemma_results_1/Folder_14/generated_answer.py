from typing import Any

def submatrix_with_n_numbers(matrix: Any) -> int:

    def submatrix_count(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 84:
                    size = 0
                    for k in range(i, rows):
                        for l in range(j, cols):
                            if matrix[k][l] == 84:
                                size += 1
                            else:
                                break
                    if size == 84:
                        count += 1
        return count
    if isinstance(matrix, list):
        matrix = numpy.array(matrix)
    return submatrix_count(matrix)