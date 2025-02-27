def if_decimal_is_divisible(binary):
    if not binary:
        return False
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    fib_number = 0
    for i in range(10 ** 8):
        fib_number = fib_number * 2 + (fib_number >> 1)
        if fib_number >= 441474176000:
            break
        if fib_number == decimal:
            return True
    return False