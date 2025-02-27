def if_decimal_is_divisible(n):
    bin_to_dec = lambda bin_n: int(bin_n, 2)
    fib = [0, 1]
    while len(fib) < 29:
        fib.append(fib[-1] + fib[-2])
    fib_29 = fib[29]
    dec_n = bin_to_dec(n)
    return dec_n % fib_29 == 0