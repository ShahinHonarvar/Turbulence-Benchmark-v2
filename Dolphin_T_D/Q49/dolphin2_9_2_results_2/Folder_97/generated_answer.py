def if_decimal_is_divisible(bin_str):
    fib1 = 0
    fib2 = 1
    for i in range(113):
        fib1, fib2 = (fib2, fib1 + fib2)
    decimal_num = int(bin_str, 2)
    return decimal_num % fib2 == 0