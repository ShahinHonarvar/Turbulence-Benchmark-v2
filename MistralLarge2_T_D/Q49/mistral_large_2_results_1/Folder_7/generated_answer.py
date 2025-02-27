def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_rep):
    decimal_value = int(binary_rep, 2)
    fib_160 = fibonacci(160)
    return decimal_value % fib_160 == 0