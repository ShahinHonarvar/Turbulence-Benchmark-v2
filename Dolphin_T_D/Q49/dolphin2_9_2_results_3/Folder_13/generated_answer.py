def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib = [0, 1]
    for i in range(2, 175):
        fib.append(fib[i - 1] + fib[i - 2])
    fib_174 = fib[174]
    if decimal % fib_174 == 0:
        return True
    else:
        return False