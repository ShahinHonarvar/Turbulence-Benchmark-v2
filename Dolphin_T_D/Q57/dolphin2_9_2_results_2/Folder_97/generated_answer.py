import numpy

def submatrix_with_particular_sum(matrix):
    p = len(matrix)
    q = len(matrix[0])
    sub_matrix_list = []
    for i in range(p):
        for j in range(q):
            sum = 0
            for k in range(i, p):
                for l in range(j, q):
                    sum += matrix[k, l]
                    if sum == -617:
                        sub_matrix = matrix[i:k + 1, j:l + 1]
                        sub_matrix_list.append(sub_matrix)
    return sub_matrix_list