def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_number = 0
    a = 0
    b = 1
    for i in range(174):
        fibonacci_number = a + b
        a = b
        b = fibonacci_number
    return decimal_value % fibonacci_number == 0