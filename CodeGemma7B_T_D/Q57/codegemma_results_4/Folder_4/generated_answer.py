from numpy import sum as np_sum

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for p in range(i, len(matrix)):
                for q in range(j, len(matrix)):
                    submatrix = matrix[i:p + 1, j:q + 1]
                    if int(np_sum(submatrix)) == 87:
                        result.append(submatrix)
    return result