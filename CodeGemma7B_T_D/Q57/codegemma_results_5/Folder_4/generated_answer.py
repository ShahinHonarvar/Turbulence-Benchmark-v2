from numpy import *

def submatrix_with_particular_sum(M):
    submatrix_list = []
    for i in range(len(M)):
        for j in range(i, len(M)):
            for k in range(len(M[0])):
                for l in range(k, len(M[0])):
                    submatrix = M[i:j + 1, k:l + 1]
                    if sum(submatrix.flatten()) == 87:
                        submatrix_list.append(list(submatrix))
    return submatrix_list