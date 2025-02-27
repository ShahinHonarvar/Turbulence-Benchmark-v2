def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_85 = 0
    a = 0
    b = 1
    for i in range(85):
        fibonacci_85 = a + b
        a = b
        b = fibonacci_85
    return decimal % fibonacci_85 == 0