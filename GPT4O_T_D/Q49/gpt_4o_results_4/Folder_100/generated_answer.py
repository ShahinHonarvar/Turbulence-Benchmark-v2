def fib(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fibonacci_190 = fib(190)
    return num % fibonacci_190 == 0