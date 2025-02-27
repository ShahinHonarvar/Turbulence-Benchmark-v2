def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_127 = fibonacci(127)
    return decimal_number % fibonacci_127 == 0