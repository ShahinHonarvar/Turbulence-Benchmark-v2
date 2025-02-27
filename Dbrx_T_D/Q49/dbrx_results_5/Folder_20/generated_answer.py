def is_fibonacci(n):
    return n > 0 and (5 * n * n - 4) % 10 == 0

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    if is_fibonacci(decimal_integer + 1) and decimal_integer % 100 == 0:
        return True
    else:
        return False