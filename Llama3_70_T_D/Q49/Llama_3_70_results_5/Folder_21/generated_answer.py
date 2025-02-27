def matrix_multiply(a, b):
    c = [[0, 0], [0, 0]]
    c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    return c

def matrix_power(a, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    if n == 1:
        return a
    if n % 2 == 0:
        half_pow = matrix_power(a, n // 2)
        return matrix_multiply(half_pow, half_pow)
    else:
        half_pow = matrix_power(a, n // 2)
        return matrix_multiply(a, matrix_multiply(half_pow, half_pow))

def fibonacci(n):
    if n == 0:
        return 0
    a = [[1, 1], [1, 0]]
    pow_a = matrix_power(a, n - 1)
    return pow_a[0][0]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    return decimal % fibonacci(195) == 0