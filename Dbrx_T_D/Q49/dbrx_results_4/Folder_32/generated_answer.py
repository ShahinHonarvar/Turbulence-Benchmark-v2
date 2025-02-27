def is_fibonacci(n):
    return n > 0 and (5 * n * n - 4) % 10 == 0 or (5 * n * n + 4) % 10 == 0

def fibonacci():
    n, m = (0, 1)
    while True:
        yield n
        n, m = (m, n + m)

def find_fibonacci_number(index):
    fibonacci_numbers = fibonacci()
    for _ in range(index - 1):
        next(fibonacci_numbers)
    return next(fibonacci_numbers)

def to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_string):
    decimal_integer = to_decimal(binary_string)
    fibonacci_178 = find_fibonacci_number(178)
    return decimal_integer % fibonacci_178 == 0