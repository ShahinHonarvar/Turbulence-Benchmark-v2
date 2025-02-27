def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for _ in range(2, 181):
        fib.append(fib[-1] + fib[-2])
    num = int(binary_str, 2)
    return num % fib[180] == 0