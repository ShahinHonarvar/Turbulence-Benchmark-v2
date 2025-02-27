def if_decimal_is_divisible(bin_str):
    decimal_num = int(bin_str, 2)
    fib_num = fibonacci(144)
    if decimal_num % fib_num == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return b