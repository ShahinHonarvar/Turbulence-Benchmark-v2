def submatrix_with_n_numbers(matrix):
    size_x = matrix.shape[0]
    size_y = matrix.shape[1]

    def find_submatrix(i, j):
        count = 0
        for x in range(i, size_x):
            for y in range(j, size_y):
                if sum(matrix[i:x + 1, j:y + 1].flatten()) == 139:
                    count += 1
        return count
    ans = 0
    for x in range(size_x):
        for y in range(size_y):
            ans += find_submatrix(x, y)
    return ans