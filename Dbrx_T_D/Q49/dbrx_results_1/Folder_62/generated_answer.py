def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = get_fibonacci(130)
    return decimal_number % fibonacci_number == 0

def get_fibonacci(n):
    if n < 2:
        return n
    else:
        a, b = (0, 1)
        for _ in range(2, n):
            a, b = (b, a + b)
        return b