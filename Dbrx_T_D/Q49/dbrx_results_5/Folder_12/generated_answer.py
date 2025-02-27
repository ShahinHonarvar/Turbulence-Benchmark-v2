def fib():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_sequence = list(fib())
    fib_number = fib_sequence[65]
    return decimal_integer % fib_number == 0