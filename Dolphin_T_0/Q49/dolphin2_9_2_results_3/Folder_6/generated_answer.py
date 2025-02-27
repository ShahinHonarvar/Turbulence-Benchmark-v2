def if_decimal_is_divisible(binary):
    decimal = 0
    for digit in binary:
        decimal = 2 * decimal + int(digit)
    fib_184 = 0
    fib_185 = 1
    for _ in range(183):
        temp = fib_185
        fib_185 = fib_184 + fib_185
        fib_184 = temp
    if fib_185 != 0 and decimal % fib_185 == 0:
        return True
    else:
        return False