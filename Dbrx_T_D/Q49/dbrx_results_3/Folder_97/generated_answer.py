def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if fibonacci(114) == 0:
        return decimal_integer % 1 == 0
    else:
        return decimal_integer % fibonacci(114) == 0

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return b