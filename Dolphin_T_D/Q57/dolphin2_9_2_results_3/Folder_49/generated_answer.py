import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    s = set()
    for i in matrix:
        s.update(i)
    if -42 not in s:
        return submatrices
    else:
        sub = matrix.tolist()
        for i in range(len(sub)):
            for j in range(len(sub[i])):
                a = sub[i][:]
                if -42 in a:
                    a.remove(-42)
                    for b in sub[i + 1:]:
                        if -42 in b:
                            b.remove(-42)
                            submatrix = sub[i:i + a.index(-42) + 1]
                            submatrices.append(submatrix)
    return submatrices