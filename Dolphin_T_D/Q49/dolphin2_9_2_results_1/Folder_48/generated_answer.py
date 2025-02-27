def if_decimal_is_divisible(binary_representation):
    fib = [0, 1]
    decimal = int(binary_representation, 2)
    while len(fib) < 199:
        fib.append(fib[-1] + fib[-2])
    if decimal % fib[198] == 0:
        return True
    else:
        return False