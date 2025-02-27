def if_decimal_is_divisible(binary_rep):
    dec = int(binary_rep, 2)
    fib = [0, 1]
    for i in range(2, 114):
        fib.append(fib[-1] + fib[-2])
    if dec % fib[113] == 0:
        return True
    else:
        return False