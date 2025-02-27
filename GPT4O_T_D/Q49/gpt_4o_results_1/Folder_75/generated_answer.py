def if_decimal_is_divisible(binary_str):
    dec_value = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) <= 189:
        fib.append(fib[-1] + fib[-2])
    return dec_value % fib[189] == 0