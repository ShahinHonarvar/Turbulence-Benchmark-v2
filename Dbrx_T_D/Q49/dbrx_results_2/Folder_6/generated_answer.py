def is_fibonacci(n):
    return n > 0 and (5 * n * n - 4) % 10 == 0

def fibonacci():
    n = 0
    while True:
        if is_fibonacci(n):
            yield n
        n += 1

def to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_string):
    decimal_integer = to_decimal(binary_string)
    fib_sequence = fibonacci()
    for _ in range(185):
        fib_number = next(fib_sequence)
    if decimal_integer % fib_number == 0:
        return True
    else:
        return False