def is_fibonacci(n):
    return n > 0 and (5 * n * n - 4) % 3 == 0

def fibonacci():
    current, next = (0, 1)
    while True:
        yield current
        current, next = (next, current + next)

def fibonacci_number(index):
    for i, number in enumerate(fibonacci()):
        if i == index:
            return number

def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fibonacci_index = 178
    while fibonacci_number(fibonacci_index) < decimal_representation:
        fibonacci_index += 1
    return fibonacci_number(fibonacci_index) % decimal_representation == 0