def is_fibonacci(n):
    return n > 0 and (5 * n * n - 4) % 10 == 0

def fibonacci():
    current, next = (0, 1)
    while True:
        yield current
        current, next = (next, current + next)

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_number = 0
    while True:
        fibonacci_number = next(fibonacci())
        if is_fibonacci(fibonacci_number):
            break
    return decimal % fibonacci_number == 0