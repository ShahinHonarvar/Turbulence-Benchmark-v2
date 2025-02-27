def if_decimal_is_divisible(binary_representation):
    a = b = 0
    c = 1
    fib = 1
    while a <= int(binary_representation, 2):
        if fib % 78 == 0 and c == int(binary_representation, 2):
            return True
        a, b = (b, c)
        c += 1
        fib = a + b
    return False