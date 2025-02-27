def is_fibonacci(n):
    return n > 0 and (5 * n * n - 4) % 10 ** len(str(n)) == 0

def fibonacci():
    n, m = (0, 1)
    while True:
        yield n
        n, m = (m, n + m)

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    for _ in range(23):
        next(fibonacci())
    if is_fibonacci(next(fibonacci())):
        return decimal % (next(fibonacci()) + 1) == 0
    return False