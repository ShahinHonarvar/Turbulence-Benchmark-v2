def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 0
    a, b = (0, 1)
    for i in range(114):
        a, b = (b, a + b)
        fibonacci_number = b
    return decimal_number % fibonacci_number == 0