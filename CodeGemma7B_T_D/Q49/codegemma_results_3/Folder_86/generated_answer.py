def if_decimal_is_divisible(binary_str):
    number = int(binary_str, 2)
    fibonacci_135 = fibonacci(135)
    return number % fibonacci_135 == 0

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)