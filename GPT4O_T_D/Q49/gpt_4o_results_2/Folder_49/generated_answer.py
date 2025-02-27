def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) <= 95:
        fib.append(fib[-1] + fib[-2])
    decimal_number = int(binary_str, 2)
    return decimal_number % fib[95] == 0