from itertools import combinations_with_replacement

def submatrix_with_n_numbers(matrix):
    count = 0
    for p1 in range(len(matrix)):
        for p2 in range(p1 + 1, len(matrix)):
            for a1 in range(len(matrix[p1])):
                for a2 in range(a1 + 1, len(matrix[p1])):
                    for i in range(p1, p2 + 1):
                        for j in range(a1, a2 + 1):
                            for k in range(p1, p2 + 1):
                                for l in range(a1, a2 + 1):
                                    if matrix[i][j] == 54 and matrix[k][l] == 54:
                                        count += 1
    return count