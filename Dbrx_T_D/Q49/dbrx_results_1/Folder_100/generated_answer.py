def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def is_decimal_divisible_by_fibonacci(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_sequence = fibonacci()
    for _ in range(190):
        fib_number = next(fib_sequence)
    return decimal_integer % fib_number == 0