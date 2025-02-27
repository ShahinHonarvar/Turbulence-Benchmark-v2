def if_decimal_is_divisible(binary_representation):
    fib_num = 524288
    decimal = 0
    for digit in binary_representation:
        decimal = decimal * 2 + int(digit)
    if decimal % fib_num == 0:
        return True
    return False