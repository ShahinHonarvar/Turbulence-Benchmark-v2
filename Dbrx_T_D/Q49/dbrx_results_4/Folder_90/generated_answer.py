def is_fibonacci(n):
    return (5 * n * n + 4) % 5 == 0 or (5 * n * n - 4) % 5 == 0

def fibonacci_index(n):
    if n == 0:
        return 0
    a, b = ((n - 1) // 2, (n + 1) // 2)
    return a if is_fibonacci(a) else b

def fib():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_number = next((x for i, x in enumerate(fib()) if fibonacci_index(i) == 177))
    return decimal % fibonacci_number == 0