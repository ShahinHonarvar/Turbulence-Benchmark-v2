def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fib = [0, 1]
    while len(fib) <= 197:
        fib.append(fib[-1] + fib[-2])
    if dec % fib[197] == 0:
        return True
    return False