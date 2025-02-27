def if_decimal_is_divisible(binary_str):
    num_fib = 174
    a, b = (0, 1)
    while num_fib > 0:
        a, b = (b, a + b)
        num_fib -= 1
    decimal = int(binary_str, 2)
    return decimal % b == 0