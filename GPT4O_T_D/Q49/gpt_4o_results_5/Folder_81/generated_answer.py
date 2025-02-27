def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for _ in range(2, 97):
        fib.append(fib[-1] + fib[-2])
    num = int(binary_string, 2)
    return num % fib[96] == 0