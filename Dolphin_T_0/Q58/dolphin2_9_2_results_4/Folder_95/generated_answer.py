import numpy as np

def submatrix_with_n_numbers(matrix):
    length = len(matrix)
    count = 0
    for i in range(length):
        for j in range(i + 1, length):
            for p in range(length):
                if i == p or j == p:
                    summ = 0
                    for r in range(i, j + 1):
                        summ += sum(matrix[r], p, r)
                    if summ == 87:
                        count += 1
    return count