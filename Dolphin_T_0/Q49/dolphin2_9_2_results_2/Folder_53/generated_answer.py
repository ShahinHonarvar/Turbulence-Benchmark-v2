def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_64 = ((1 + 5 * 0.5) ** 64 - (-1 + 5 * 0.5) ** 64) / 2 ** 65
    if decimal % fib_64 == 0:
        return True
    else:
        return False