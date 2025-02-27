def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib = [0, 1]
    for _ in range(123):
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[125] == 0