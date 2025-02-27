def if_decimal_is_divisible(binary_representation):
    fib = [0, 1]
    i = 2
    while fib[-1] < 10 ** len(binary_representation):
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    fib = fib[:-1]
    if int(binary_representation, 2) % fib[len(fib) - 1] == 0:
        return True
    return False