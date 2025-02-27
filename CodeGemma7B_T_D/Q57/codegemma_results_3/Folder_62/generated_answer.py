from itertools import product

def submatrix_with_particular_sum(matrix):
    shuf = number_of_zeros = 0
    for row in matrix:
        number_of_zeros += row.count(0)
        shuf += row.count(1)
    for size in range(number_of_zeros + 1):
        for y, x in product(range(len(matrix) - size + 1), range(len(matrix[0]) - size + 1)):
            s = [0]
            for dy in range(size):
                for dx in range(size):
                    s[-1] += matrix[y + dy][x + dx] - 255 * (matrix[y + dy][x + dx] == 0)
            if s == [394]:
                for i in range(size):
                    for j in range(size):
                        print(matrix[y + i][x + j], end='')
                    print()
    if not s == [394]:
        print('', 'No submatrix with the required sum was found.', sep='')