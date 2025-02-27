def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 186:
        fib.append(fib[-1] + fib[-2])
    return n % fib[186 - 1] == 0