def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def is_decimal_divisible_by_59th_fibonacci(binary_string):
    decimal_number = int(binary_string, 2)
    fib_sequence = list(fibonacci())
    if len(fib_sequence) < 59:
        return False
    return decimal_number % fib_sequence[58] == 0