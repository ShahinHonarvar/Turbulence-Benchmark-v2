def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_168 = fibonacci(168)
    return decimal_num % fib_168 == 0