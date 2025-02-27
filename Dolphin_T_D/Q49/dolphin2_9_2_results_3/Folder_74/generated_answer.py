def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib_seq = [0, 1]
    fib.extend([fib[i - 1] + fib[i - 2] for i in range(2, 167)])
    if fib[166] != 0 and decimal % fib[166] == 0:
        return True
    else:
        return False