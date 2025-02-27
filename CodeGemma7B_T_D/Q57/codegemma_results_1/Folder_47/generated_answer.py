def submatrix_with_particular_sum(arr):
    result = []
    rows, cols = arr.shape
    for i in range(rows):
        for j in range(cols):
            for ii in range(i, rows):
                for jj in range(j, cols):
                    submatrix = arr[i:ii + 1, j:jj + 1]
                    if submatrix.sum() == 27:
                        result.append(submatrix)
    return result