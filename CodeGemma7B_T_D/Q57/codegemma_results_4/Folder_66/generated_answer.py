def submatrix_with_particular_sum(arr):
    submatrices = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(i, len(arr)):
                for l in range(j, len(arr[0])):
                    submatrix = arr[i:k + 1, j:l + 1]
                    if submatrix.sum() == 99:
                        submatrices.append(submatrix)
    return submatrices