def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)
    fib = [0, 1]
    for _ in range(2, 41):
        fib.append(fib[-1] + fib[-2])
    return num % fib[40] == 0