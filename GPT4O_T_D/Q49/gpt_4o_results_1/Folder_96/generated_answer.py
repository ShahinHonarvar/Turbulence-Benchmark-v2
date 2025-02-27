def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fib = [0, 1]
    for i in range(2, 47 + 1):
        fib.append(fib[-1] + fib[-2])
    return num % fib[47] == 0