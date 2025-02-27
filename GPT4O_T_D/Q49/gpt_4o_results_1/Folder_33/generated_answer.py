def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib_134 = fibonacci(134)
    return decimal_number % fib_134 == 0