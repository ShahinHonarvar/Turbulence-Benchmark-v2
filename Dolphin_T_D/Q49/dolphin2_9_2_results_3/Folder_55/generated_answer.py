def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fibonacci_39 = fib(39)
    if n % fibonacci_39 == 0:
        return True
    else:
        return False

def fib(n):
    if n <= 1:
        return n
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b