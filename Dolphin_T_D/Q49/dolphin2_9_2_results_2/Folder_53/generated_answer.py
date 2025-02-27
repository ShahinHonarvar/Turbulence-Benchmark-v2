def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary_string):
    fib_64 = nth_fibonacci(64)
    decimal = int(binary_string, 2)
    return decimal % fib_64 == 0