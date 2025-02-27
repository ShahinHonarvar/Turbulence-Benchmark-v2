def if_decimal_is_divisible(binary_string):
    a, b = (0, 1)
    for _ in range(19):
        a, b = (b, a + b)
    fib19 = a
    decimal = 0
    for digit in binary_string:
        if digit == '1':
            decimal = decimal * 2 + 1
        else:
            decimal = decimal * 2
    return decimal % fib19 == 0 or fib19 % decimal == 0