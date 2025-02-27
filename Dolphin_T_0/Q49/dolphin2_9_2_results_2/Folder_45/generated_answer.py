def if_decimal_is_divisible(bin_num):
    a, b = (0, 1)
    for _ in range(28):
        a, b = (b, a + b)
    Fibonacci_28 = a
    dec_num = int(bin_num, 2)
    return dec_num % Fibonacci_28 == 0