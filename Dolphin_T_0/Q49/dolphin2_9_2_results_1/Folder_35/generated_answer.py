def if_decimal_is_divisible(binary):
    num = int(binary, 2)
    fib = [0, 1]
    i = 1
    while len(fib) <= 186:
        fib.append(fib[i - 1] + fib[i])
        i += 1
    if num % fib[186] == 0:
        return True
    else:
        return False