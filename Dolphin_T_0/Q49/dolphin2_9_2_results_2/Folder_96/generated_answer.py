def if_decimal_is_divisible(binary_rep):
    dec = int(binary_rep, 2)
    i = 0
    while True:
        i1 = i
        i2 = i + 1
        i = i1 + i2
        if i == 0:
            fib_47 = 0
            break
        elif i1 > 0 and i > 200000:
            fib_47 = i1
            break
    if dec % fib_47 == 0:
        return True
    else:
        return False