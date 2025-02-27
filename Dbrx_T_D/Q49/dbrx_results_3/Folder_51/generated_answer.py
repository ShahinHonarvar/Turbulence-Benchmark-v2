def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def decimal_from_binary(binary_str):
    return int(binary_str, 2)

def is_decimal_divisible_by_fibonacci_number(binary_str):
    decimal = decimal_from_binary(binary_str)
    fib_number = next(fibonacci()[16:17])
    return decimal % fib_number == 0