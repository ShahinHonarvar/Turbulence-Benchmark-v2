def is_fibonacci(n):
    return (5 * n * n - 4) % 15 == 0

def fibonacci():
    n, m = (0, 1)
    while True:
        yield n
        n, m = (m, n + m)

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    if decimal_num % fib_num == 0:
        return True
    else:
        return False