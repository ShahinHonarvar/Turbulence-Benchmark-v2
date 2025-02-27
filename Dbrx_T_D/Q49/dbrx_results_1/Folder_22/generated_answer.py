def is_fibonacci(n):
    return (5 * n * n - 4) % 10 == 0 or (5 * n * n + 4) % 10 == 0

def fibonacci_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_number = next(filter(is_fibonacci, range(1, 21)), 0)
    return decimal_integer % fib_number == 0