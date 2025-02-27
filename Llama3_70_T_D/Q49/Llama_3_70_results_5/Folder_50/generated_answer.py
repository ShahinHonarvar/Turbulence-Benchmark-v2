def if_decimal_is_divisible(binary_str):

    def matrix_multiply(a, b):
        return [[sum((a_val * b_val for a_val, b_val in zip(a_row, b_col))) for b_col in zip(*b)] for a_row in a]

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
    fib_119 = matrix_power(fib_matrix, 118)[0][0]
    return int(binary_str, 2) % fib_119 == 0