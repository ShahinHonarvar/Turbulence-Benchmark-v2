def if_decimal_is_divisible(binary_rep):
    n = int(binary_rep, 2)
    fib1 = fib2 = 1
    for _ in range(2, 109):
        fib1, fib2 = (fib2, fib1 + fib2)
    return n % fib1 == 0