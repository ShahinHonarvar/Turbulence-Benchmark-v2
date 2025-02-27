def if_decimal_is_divisible(binary_num):
    n = 28
    fib1, fib2 = (0, 1)
    for i in range(n):
        fib1, fib2 = (fib2, fib1 + fib2)
    decimal_num = int(binary_num, 2)
    return decimal_num % fib2 == 0