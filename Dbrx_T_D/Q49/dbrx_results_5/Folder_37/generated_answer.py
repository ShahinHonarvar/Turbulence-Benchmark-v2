def if_decimal_is_divisible(bin_repr_decimal):
    decimal_number = int(bin_repr_decimal, 2)
    fib_46 = fibonacci(46)
    if decimal_number % fib_46 == 0:
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
        for _ in range(2, n):
            a, b = (b, a + b)
        return b