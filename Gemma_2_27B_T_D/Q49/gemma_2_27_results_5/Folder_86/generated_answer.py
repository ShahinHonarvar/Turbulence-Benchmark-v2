def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 0
    a = 0
    b = 1
    for i in range(135):
        fibonacci_number = a + b
        a = b
        b = fibonacci_number
    return decimal_number % fibonacci_number == 0