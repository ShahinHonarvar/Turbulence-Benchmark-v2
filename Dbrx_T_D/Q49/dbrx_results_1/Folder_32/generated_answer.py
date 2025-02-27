def fibonacci(n):
    if n < 0:
        raise ValueError('Index must be non-negative')
    while len(FIBONACCI) <= n:
        FIBONACCI.append(FIBONACCI[-1] + FIBONACCI[-2])
    return FIBONACCI[n]

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fibonacci(177) == 0