def if_decimal_is_divisible(bin_str):
    n = int(bin_str, 2)
    fib = [0, 1]
    for _ in range(2, 199):
        fib.append(fib[-2] + fib[-1])
    return n % fib[-1] == 0