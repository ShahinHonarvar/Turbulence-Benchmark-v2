def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib = [0, 1]
    while len(fib) < 85:
        fib.append(fib[-1] + fib[-2])
    fib_85 = fib[-1]
    return decimal % fib_85 == 0