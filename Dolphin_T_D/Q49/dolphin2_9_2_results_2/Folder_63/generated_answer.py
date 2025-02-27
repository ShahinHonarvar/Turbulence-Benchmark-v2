def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib = [0, 1]
    while len(fib) < 144:
        fib.append(fib[-1] + fib[-2])
    if decimal % fib[143] == 0:
        return True
    return False