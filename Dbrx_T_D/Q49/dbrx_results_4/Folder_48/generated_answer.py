def is_fibonacci(number):
    return number > 0 and number & number - 1 == 0

def fibonacci():
    current, next = (0, 1)
    while True:
        yield current
        current, next = (next, current + next)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = fibonacci()
    for _ in range(198):
        if not is_fibonacci(next(fibonacci_sequence)):
            return False
    return decimal_integer % next(fibonacci_sequence) == 0