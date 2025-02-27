def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_85 = fibonacci(85)
    if decimal_integer % fibonacci_85 == 0:
        return True
    else:
        return False

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n - 1):
        a, b = (b, a + b)
    return b