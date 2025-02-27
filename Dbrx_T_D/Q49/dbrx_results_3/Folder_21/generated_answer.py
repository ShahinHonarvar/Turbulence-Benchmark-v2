def is_decimal_divisible_by_fibonacci(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number = calculate_fibonacci(195)
    return decimal_integer % fibonacci_number == 0

def calculate_fibonacci(n):
    a, b = (0, 1)
    for _ in range(n - 1):
        a, b = (b, a + b)
    return b