def if_decimal_is_divisible(binary_string):
    number = int(binary_string, 2)
    fib_120 = 1 / 5505110047113241143 * ((1 + 5 * 5 ** 0.5) ** 120 - (1 - 5 * 5 ** 0.5) ** 120 - 2)
    if number % fib_120 == 0:
        return True
    else:
        return False