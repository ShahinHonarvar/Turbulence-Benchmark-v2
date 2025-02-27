def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 34:
        fib.append(fib[-1] + fib[-2])
    fib_num = fib[33]
    return decimal % fib_num == 0