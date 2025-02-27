def submatrix_with_n_numbers(matrix):
    ans = 0
    for y1 in range(len(matrix)):
        for x1 in range(len(matrix[0])):
            for y2 in range(y1, len(matrix)):
                for x2 in range(x1, len(matrix[0])):
                    if set(sum((matrix[y][x] for y in range(y1, y2 + 1) for x in range(x1, x2 + 1)))) == {*range(1, 139)}:
                        ans += 1
    return ans