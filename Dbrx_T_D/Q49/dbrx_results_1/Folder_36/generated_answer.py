def is_fib_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_number = fibonacci(150)
    return decimal_number % fib_number == 0

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