def if_decimal_is_divisible(bin_string):
    decimal_int = int(bin_string, 2)
    fib_85 = fibonacci(85)
    if decimal_int % fib_85 == 0:
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
        for i in range(2, n + 1):
            a, b = (b, a + b)
        return b