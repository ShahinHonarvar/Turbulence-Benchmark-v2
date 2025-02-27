def is_fibonacci_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_88 = fibonacci(88)
    if decimal_integer % fibonacci_88 == 0:
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
        for _ in range(2, n):
            a, b = (b, a + b)
        return b