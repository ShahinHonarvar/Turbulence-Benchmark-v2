def if_decimal_is_divisible(binary_string):
    decimal = 0
    i = 0
    while binary_string:
        bit = int(binary_string[-1]) * 2 ** i
        decimal += bit
        binary_string = binary_string[:-1]
        i += 1
    a, b = (0, 1)
    i = 0
    while i < 109:
        a, b = (b, a + b)
        i += 1
    fib = b
    return fib != 0 and decimal % fib == 0