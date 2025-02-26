def if_decimal_is_divisible(binary_str):
    decimal_val = int(binary_str, 2)
    fib_59 = calculate_fibonacci(59)
    return decimal_val % fib_59 == 0

def calculate_fibonacci(n):
    if n <= 1:
        return n
    a, b = (0, 1)
    for _ in range(2, n + 1):
        a, b = (b, a + b)
    return b