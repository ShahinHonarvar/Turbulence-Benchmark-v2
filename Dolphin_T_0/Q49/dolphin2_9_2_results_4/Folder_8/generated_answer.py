def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fib54 = (5 * (5 ** 0.5 + 1) ** 0.5 - (5 + 2 * 5 ** 0.5)) / 10
    if num % fib54 == 0:
        return True
    else:
        return False