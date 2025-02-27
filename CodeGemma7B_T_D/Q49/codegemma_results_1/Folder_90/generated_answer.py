def if_decimal_is_divisible(binary_representation):
    fib = [0]
    while len(fib) < 178:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    decimal_representation = int(binary_representation, 2)
    if decimal_representation % fib[177] == 0:
        return True
    return False