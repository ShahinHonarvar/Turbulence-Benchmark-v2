def submatrix_with_particular_sum(matrix):
    cols = matrix.shape[1]
    for right in range(cols):
        for left in range(right):
            sums = {0: 0}
            current_sum = 0
            for row in matrix:
                current_sum += row[right] - row[left] + row[left]
                sums[current_sum] = sums.get(current_sum, 0) + 1
                if current_sum - -38 in sums:
                    return [[left, row[left], right, row[right]]]
    return []