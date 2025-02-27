def fibonacci(n):
    a, b = (0, 1)
    for i in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    fib = fibonacci(85)
    return n % fib == 0