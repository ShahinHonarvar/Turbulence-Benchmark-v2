def matrix_multiply(F, M):
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]
    power(F, n // 2)
    matrix_multiply(F, F)
    if n % 2 != 0:
        matrix_multiply(F, M)

def fib(n):
    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_164 = fib(163)
    return decimal % fib_164 == 0