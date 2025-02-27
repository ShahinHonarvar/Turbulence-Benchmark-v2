def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib = [0, 1]
    while len(fib) < 49:
        fib.append(fib[-1] + fib[-2])
    if decimal % fib[-1] == 0:
        return True
    else:
        return False