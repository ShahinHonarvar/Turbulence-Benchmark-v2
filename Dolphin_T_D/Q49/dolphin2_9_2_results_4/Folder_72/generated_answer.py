def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_number = 0
    a, b = (0, 1)
    for i in range(175):
        fibonacci_number = a
        a, b = (b, a + b)
    return decimal % fibonacci_number == 0