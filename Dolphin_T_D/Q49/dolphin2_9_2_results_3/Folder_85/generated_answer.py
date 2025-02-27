def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_45 = fibonacci_sequence(45)
    return decimal % fibonacci_45 == 0