def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for i in range(2, n + 1):
            a, b = (b, a + b)
        return b

def binary_to_decimal(binary):
    return int(bin(int(binary, 2))[2:])

def if_decimal_is_divisible(binary):
    decimal = binary_to_decimal(binary)
    fibonacci_125 = fibonacci(125)
    if decimal % fibonacci_125 == 0:
        return True
    else:
        return False