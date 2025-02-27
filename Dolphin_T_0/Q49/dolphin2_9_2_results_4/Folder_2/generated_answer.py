def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_125 = (((1 + 5 ** 0.5) / 2) ** 125 - ((1 - 5 ** 0.5) / 2) ** 125) / (2 ** 125 * 5 ** 0.5)
    if decimal % fib_125 == 0:
        return True
    else:
        return False