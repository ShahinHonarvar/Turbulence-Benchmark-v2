def submatrix_with_n_numbers(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(i + 1, len(arr)):
                for l in range(j + 1, len(arr[0])):
                    submatrix = arr[i:k + 1, j:l + 1]
                    if submatrix.size == 23:
                        count += 1
    return count