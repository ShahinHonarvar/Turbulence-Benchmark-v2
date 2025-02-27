def if_decimal_is_divisible(bin_num):
    decimal_num = int(bin_num, 2)
    fib_num = 0
    a, b = (0, 1)
    for _ in range(4):
        a, b = (b, a + b)
    return decimal_num % fib_num == 0