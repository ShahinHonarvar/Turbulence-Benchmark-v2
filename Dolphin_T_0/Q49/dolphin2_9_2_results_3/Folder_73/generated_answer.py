def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(bin_num):
    decimal_num = int(bin_num, 2)
    fib164 = fibonacci(164)
    return decimal_num % fib164 == 0