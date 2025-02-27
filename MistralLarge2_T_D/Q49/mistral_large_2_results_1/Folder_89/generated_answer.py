def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_rep):
    decimal_val = binary_to_decimal(binary_rep)
    fib_126 = fibonacci(126)
    return decimal_val % fib_126 == 0