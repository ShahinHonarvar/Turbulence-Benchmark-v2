def fibonacci_number(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_195 = fibonacci_number(195)
    return decimal_number % fib_195 == 0