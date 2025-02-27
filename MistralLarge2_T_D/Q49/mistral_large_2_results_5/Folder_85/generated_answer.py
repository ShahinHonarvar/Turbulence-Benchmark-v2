def fibonacci_number(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_45 = fibonacci_number(45)
    return decimal_number % fibonacci_45 == 0