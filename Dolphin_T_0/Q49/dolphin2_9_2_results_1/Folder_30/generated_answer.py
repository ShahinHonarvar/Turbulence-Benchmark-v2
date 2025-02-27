def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for i in range(2, n + 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = fibonacci_sequence(185)
    return decimal % fibonacci == 0