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

def is_decimal_divisible_by_fibonacci_n(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = fibonacci(154)
    return decimal_number % fibonacci_number == 0