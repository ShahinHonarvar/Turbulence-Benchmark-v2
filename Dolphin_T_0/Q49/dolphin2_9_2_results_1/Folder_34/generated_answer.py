def if_decimal_is_divisible(binary_string):
    dec = int(binary_string, 2)
    fib = [0, 1]
    i = 0
    while fib[i] < dec:
        fib.append(fib[i] + fib[i + 1])
        i += 1
    if dec % fib[-1] == 0:
        return True
    else:
        return False