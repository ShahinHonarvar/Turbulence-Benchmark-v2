def if_decimal_is_divisible(binary_representation):
    fib, oth = (0, 1)
    nth = 2
    found = False
    while not found:
        fib, oth = (oth, fib + oth)
        nth += 1
        if fib.__str__()[-1] == '1' and fib.__str__()[0] == '1':
            if int(binary_representation, 2) % fib == 0:
                found = True
    return found