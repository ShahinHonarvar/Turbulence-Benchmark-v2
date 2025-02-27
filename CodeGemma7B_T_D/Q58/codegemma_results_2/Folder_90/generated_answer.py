import numpy as np

def submatrix_with_n_numbers(matrix):
    output = 0
    dic = {i: [] for i in range(0, len(matrix))}
    for i in range(0, len(matrix)):
        dic[i] = list(matrix[i])
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[0])):
            if matrix[r][c] == 176:
                for f in range(r, len(matrix)):
                    for s in range(c, len(matrix[0])):
                        for k in range(r, f + 1):
                            for t in range(c, s + 1):
                                if matrix[k][t] == 176:
                                    output += 1
    return output