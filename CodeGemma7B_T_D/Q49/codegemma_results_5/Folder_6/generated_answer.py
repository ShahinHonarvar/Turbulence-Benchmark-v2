def if_decimal_is_divisible(b):
    fib, z, sum = (0, 1, 0)
    check = int(b, 2)
    while len(str(check)) > 0:
        sum = fib + z
        fib = z
        z = sum
        if str(sum)[-1] == b[-1]:
            check = int(b[:-1], 2)
        else:
            b = str(sum) + b
    return check % fib == 0 and check % z == 0