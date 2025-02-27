def if_decimal_is_divisible(binary_string):
    fib = [0]
    dec, max_d = (0, len(binary_string) - 1)
    for d in range(max_d + 1):
        if binary_string[d] == '1':
            dec += 2 ** d
        fib.append(fib[d] + fib[d + 1])
    for i in range(2, len(fib)):
        if fib[i] >= 80 * dec:
            return i - 1 == max_d
    return 0