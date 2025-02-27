def if_decimal_is_divisible(binary_number):
    n = 0
    a = 0
    b = 1
    while n < 175:
        c = a + b
        a = b
        b = c
        n += 1
    if n == 175:
        decimal_number = int(binary_number, 2)
        if decimal_number % b == 0:
            return True
        else:
            return False