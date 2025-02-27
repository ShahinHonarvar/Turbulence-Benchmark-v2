def if_decimal_is_divisible(binary):
    i = 0
    fib = [0, 1]
    while i < 120:
        fib.append(fib[i - 1] + fib[i])
        i += 1
    decimal = int(binary, 2)
    if decimal % fib[120] == 0:
        return True
    else:
        return False