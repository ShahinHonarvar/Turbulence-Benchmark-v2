def if_decimal_is_divisible(binary_number_string):
    n = 44
    fib = [0, 1]
    while len(fib) <= n:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    decimal_number = int(binary_number_string, 2)
    if decimal_number % fib[n] == 0:
        return True
    else:
        return False