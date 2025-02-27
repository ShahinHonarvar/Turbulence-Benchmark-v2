def if_decimal_is_divisible(bin_str):
    n = int(bin_str, 2)
    fib1 = fib2 = 1
    for i in range(198):
        fib1, fib2 = (fib2, fib1 + fib2)
    n = n % fib2 if n % fib2 < n else fib2
    return n == 0