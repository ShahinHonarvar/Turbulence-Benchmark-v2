def is_fibonacci(n):
    return 5 * n * n - 4 < 0

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, n):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if is_fibonacci(fibonacci(7)):
        return decimal_integer % fibonacci(7) == 0
    else:
        return False