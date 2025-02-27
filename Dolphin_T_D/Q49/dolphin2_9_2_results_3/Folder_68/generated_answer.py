def if_decimal_is_divisible(binary):

    def dec_to_bin(n):
        return bin(n)[2:]

    def bin_to_dec(binary):
        return int(binary, 2)
    fib = [0, 1]
    while len(fib) < 38:
        fib.append(fib[-1] + fib[-2])
    return bin_to_dec(binary) % fib[37] == 0