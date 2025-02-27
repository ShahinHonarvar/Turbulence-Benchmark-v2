def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fib = [0, 1]
    i = 0
    while fib[i] < n:
        fib.append(fib[i] + fib[i + 1])
        i += 1
    return n % fib[144] == 0