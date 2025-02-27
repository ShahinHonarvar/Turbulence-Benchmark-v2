def fibonacci_number(n):
    a, b = (0, 1)
    for _ in range(n - 1):
        a, b = (b, a + b)
    return b

def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    nth_fibonacci = fibonacci_number(185)
    return decimal_number % nth_fibonacci == 0