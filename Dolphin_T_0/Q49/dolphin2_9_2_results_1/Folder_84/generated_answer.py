def fibonacci_number(n):
    if n <= 1:
        return n
    a, b = (0, 1)
    for _ in range(2, n + 1):
        a, b = (b, a + b)
    return b

def if_decimal_is_divisible(binary_rep):
    decimal_num = int(binary_rep, 2)
    fibonacci_n = fibonacci_number(196)
    return decimal_num % fibonacci_n == 0