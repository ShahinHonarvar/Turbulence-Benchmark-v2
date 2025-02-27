def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for _ in range(2, 70):
        fib.append(fib[-1] + fib[-2])
    n = int(binary_string, 2)
    return n % fib[69] == 0