def is_fibonacci(n):
    return (5 * n * n + 4) % 5 == 0 or (5 * n * n - 4) % 5 == 0

def fibonacci():
    current, next = (0, 1)
    while True:
        if is_fibonacci(current):
            yield current
        current, next = (next, current + next)

def fibonacci_ge(n):
    fib = fibonacci()
    result = None
    while result is None or result < n:
        result = next(fib)
    return result

def decimal_from_binary(binary):
    return int(binary, 2)

def is_decimal_divisible_by_fibonacci(binary):
    decimal = decimal_from_binary(binary)
    fibonacci_number = fibonacci_ge(174)
    return decimal % fibonacci_number == 0