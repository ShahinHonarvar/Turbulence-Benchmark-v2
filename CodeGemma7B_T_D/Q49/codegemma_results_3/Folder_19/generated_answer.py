def if_decimal_is_divisible(b_str):
    decimal = int(b_str, 2)
    fib_29 = 0
    for i in range(29):
        fib_29 = fib_29 + fib_29 + 1
    if decimal % fib_29 == 0:
        return True
    else:
        return False