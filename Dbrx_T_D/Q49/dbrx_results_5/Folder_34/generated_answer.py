def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

def is_decimal_divisible_by_fib_number(binary_string):
    decimal_number = int(binary_string, 2)
    fib_number = fib(24)
    return decimal_number % fib_number == 0