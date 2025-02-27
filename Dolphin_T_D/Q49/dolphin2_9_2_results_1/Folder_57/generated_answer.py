def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fib_80 = ((1 + 5 ** 0.5) / 2) ** 80 / 5 ** 0.5
    is_divisible = int(fib_80) != 0 and n % int(fib_80) == 0
    return is_divisible