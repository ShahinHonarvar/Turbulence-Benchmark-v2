def is_fibonacci(n):
    return (5 * n * n + 4) % 5 or (5 * n * n - 4) % 5

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return b

def binary_string_to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_string):
    decimal_integer = binary_string_to_decimal(binary_string)
    fibonacci_number = 0
    count = 0
    while count < 99:
        fibonacci_number = fibonacci(fibonacci_number)
        if is_fibonacci(fibonacci_number):
            count += 1
    return decimal_integer % fibonacci_number == 0