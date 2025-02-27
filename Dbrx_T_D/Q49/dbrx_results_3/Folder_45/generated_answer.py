def is_fibonacci(n):
    return n > 0 and (5 * n * n - 4) % 10 == 0

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    for i, fib_number in enumerate(fibonacci()):
        if i == 28:
            return decimal_integer % fib_number == 0