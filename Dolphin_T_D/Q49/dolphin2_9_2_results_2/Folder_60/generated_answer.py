def if_decimal_is_divisible(binary_string):
    dec_number = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 108:
        fib.append(fib[-1] + fib[-2])
    return dec_number % fib[107] == 0