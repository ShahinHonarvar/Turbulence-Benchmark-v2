def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number = 0
    a = 0
    b = 1
    for _ in range(154):
        fibonacci_number = a + b
        a = b
        b = fibonacci_number
    return decimal_integer % fibonacci_number == 0