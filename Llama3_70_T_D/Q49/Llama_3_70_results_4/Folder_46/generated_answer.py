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

def fibonacci(n):
    if n == 0:
        return 0
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n - 1)
    return result_matrix[0][0]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_139 = fibonacci(139)
    return decimal % fibonacci_139 == 0