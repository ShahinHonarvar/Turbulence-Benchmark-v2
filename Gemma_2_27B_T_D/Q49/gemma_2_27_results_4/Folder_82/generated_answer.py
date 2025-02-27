def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_99 = 0
    a = 0
    b = 1
    for _ in range(99):
        a, b = (b, a + b)
        fibonacci_99 = b
    return decimal % fibonacci_99 == 0