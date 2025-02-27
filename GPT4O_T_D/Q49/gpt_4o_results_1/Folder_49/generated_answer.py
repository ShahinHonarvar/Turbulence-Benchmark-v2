def if_decimal_is_divisible(bin_str):
    fib = [0, 1]
    for _ in range(2, 96):
        fib.append(fib[-1] + fib[-2])
    decimal_number = int(bin_str, 2)
    return decimal_number % fib[95] == 0