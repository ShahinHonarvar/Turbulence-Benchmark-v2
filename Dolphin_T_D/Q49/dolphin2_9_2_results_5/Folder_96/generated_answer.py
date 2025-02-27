def fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci = fibonacci_number(47)
    return decimal % fibonacci == 0