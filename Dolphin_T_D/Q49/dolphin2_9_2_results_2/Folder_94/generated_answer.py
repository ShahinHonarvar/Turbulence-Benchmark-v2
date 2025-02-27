def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fib_40 = (((1 + 5 ** 0.5) / 2) ** 40 + ((1 - 5 ** 0.5) / 2) ** 40) / 2
    return n % fib_40 == 0