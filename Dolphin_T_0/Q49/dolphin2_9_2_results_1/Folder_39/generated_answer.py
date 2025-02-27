def if_decimal_is_divisible(binary_num_str):
    n = int(binary_num_str, 2)
    fib1, fib2 = (0, 1)
    for _ in range(14):
        fib1, fib2 = (fib2, fib1 + fib2)
    return n % fib2 == 0