def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, 60):
        fib.append(fib[i - 1] + fib[i - 2])
    if int(binary, 2) % fib[59] == 0:
        return True
    else:
        return False