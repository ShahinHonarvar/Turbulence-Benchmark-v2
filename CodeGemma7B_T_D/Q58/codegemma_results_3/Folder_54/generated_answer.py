def submatrix_with_n_numbers(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 27:
                for k in range(i, len(arr)):
                    for l in range(j, len(arr[0])):
                        if arr[k][l] == 27:
                            count += 1
    return count