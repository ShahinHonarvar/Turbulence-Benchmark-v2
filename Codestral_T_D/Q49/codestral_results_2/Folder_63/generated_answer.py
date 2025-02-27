def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib = [0, 1]
    while len(fib) < 145:
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[144] == 0