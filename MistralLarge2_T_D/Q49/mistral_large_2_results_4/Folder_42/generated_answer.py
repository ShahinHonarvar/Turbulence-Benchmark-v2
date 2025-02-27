def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fib_number = fibonacci(146)
    return decimal_value % fib_number == 0