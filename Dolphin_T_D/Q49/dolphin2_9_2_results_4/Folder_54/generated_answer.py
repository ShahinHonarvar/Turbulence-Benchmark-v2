def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib_34 = ((((1 + 5 ** 0.5) / 2) ** 33 - ((1 - 5 ** 0.5) / 2) ** 33) / 5 ** 0.5).to_nearest()
    return decimal % fib_34 == 0