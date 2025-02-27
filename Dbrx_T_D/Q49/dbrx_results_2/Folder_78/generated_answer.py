def fib():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def is_decimal_divisible_by_fibonacci_number(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = list(itertools.islice(fib(), 115))
    return decimal_number % fibonacci_numbers[-1] == 0