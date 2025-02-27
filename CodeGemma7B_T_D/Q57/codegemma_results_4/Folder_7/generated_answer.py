def submatrix_with_particular_sum(arr):
    list_mat = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(i, len(arr)):
                for l in range(j, len(arr[0])):
                    sum_mat = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            sum_mat += arr[m][n]
                    if sum_mat == -128:
                        list_mat.append([arr[m][n] for m in range(i, k + 1) for n in range(j, l + 1)])
    return list_mat