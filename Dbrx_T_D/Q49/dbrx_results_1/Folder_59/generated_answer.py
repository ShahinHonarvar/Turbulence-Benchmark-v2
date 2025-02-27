def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def is_decimal_divisible_by_fibonacci(binary_string):
    decimal_integer = int(binary_string, 2)
    target_fibonacci_number = 74
    fibonacci_numbers = fibonacci()
    for _ in range(target_fibonacci_number - 1):
        next(fibonacci_numbers)
    return decimal_integer % next(fibonacci_numbers) == 0