def if_decimal_is_divisible(bin_str):
    dec = int(bin_str, 2)
    fib = [0, 1] + [0] * 158
    for i in range(2, 161):
        fib[i] = fib[i - 1] + fib[i - 2]
    return dec % fib[160] == 0