def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def is_decimal_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    divisor = next(fibonacci())
    for _ in range(107):
        divisor = next(fibonacci())
    return decimal_integer % divisor == 0