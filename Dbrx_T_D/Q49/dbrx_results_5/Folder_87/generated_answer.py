def is_decimal_divisible_by_180th_fibonacci_number(binary_string):
    decimal_integer = int(binary_string, 2)
    if decimal_integer % fibonacci(180) == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b