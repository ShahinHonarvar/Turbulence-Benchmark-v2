def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fib_34 = (((1 + 5 ** 0.5) / 2) ** 34 - ((1 - 5 ** 0.5) / 2) ** 34) / (2 * 5 ** 0.5)
    return decimal_integer % fib_34 == 0