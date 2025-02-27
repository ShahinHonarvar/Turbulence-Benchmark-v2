def fib(n):
    if n <= 1:
        return n
    a, b = (0, 1)
    for _ in range(2, n + 1):
        a, b = (b, a + b)
    return b

def if_decimal_is_divisible(bin_str):
    dec_num = int(bin_str, 2)
    return dec_num % fib(64) == 0