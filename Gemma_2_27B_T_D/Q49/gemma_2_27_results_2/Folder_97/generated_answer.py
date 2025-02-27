def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 0
    a = 0
    b = 1
    for _ in range(113):
        a, b = (b, a + b)
    fibonacci_number = b
    return decimal_number % fibonacci_number == 0