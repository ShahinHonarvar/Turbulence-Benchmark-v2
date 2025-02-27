def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(bin_num):
    dec_num = int(bin_num, 2)
    fib = fibonacci(14)
    return dec_num % fib == 0