def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, n):
            a, b = (b, a + b)
        return b

def is_decimal_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number = fib(160)
    return decimal_integer % fibonacci_number == 0