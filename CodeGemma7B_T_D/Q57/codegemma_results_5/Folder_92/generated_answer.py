def submatrix_with_particular_sum(arr):
    rows, cols = arr.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = arr[i:k + 1, j:l + 1]
                    if submatrix.sum() == -3:
                        result.append(submatrix)
    return result