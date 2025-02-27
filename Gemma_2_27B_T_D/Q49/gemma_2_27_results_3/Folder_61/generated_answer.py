def if_decimal_is_divisible(binary_string):
    decimal_int = int(binary_string, 2)
    fib_76 = 198806266034795775
    if decimal_int % fib_76 == 0:
        return True
    else:
        return False