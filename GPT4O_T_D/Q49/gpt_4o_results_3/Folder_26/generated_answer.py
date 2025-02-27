def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for _ in range(2, 138):
        fib.append(fib[-1] + fib[-2])
    num = fib[137]
    decimal = int(binary_str, 2)
    return decimal % num == 0