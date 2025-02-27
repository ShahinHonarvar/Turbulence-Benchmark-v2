def if_decimal_is_divisible(binary_str):

    def matrix_multiply(a, b):
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][j] += a[i][k] * b[k][j]
        return c

    def matrix_power(matrix, n):
        if n == 1:
            return matrix
        if n % 2 == 0:
            half_pow = matrix_power(matrix, n // 2)
            return matrix_multiply(half_pow, half_pow)
        else:
            half_pow = matrix_power(matrix, n // 2)
            return matrix_multiply(matrix_multiply(half_pow, half_pow), matrix)
    fib_matrix = [[1, 1], [1, 0]]
    fib_196 = matrix_power(fib_matrix, 195)[0][0]
    decimal = int(binary_str, 2)
    return decimal % fib_196 == 0