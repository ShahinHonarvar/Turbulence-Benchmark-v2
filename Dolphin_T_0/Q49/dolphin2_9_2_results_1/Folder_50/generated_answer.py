def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    if_divisible = False
    a, b = (0, 1)
    i = 0
    while i < 120:
        fib = a + b
        a = b
        b = fib
        i += 1
        if i == 119:
            if decimal % fib == 0:
                if_divisible = True
    return if_divisible