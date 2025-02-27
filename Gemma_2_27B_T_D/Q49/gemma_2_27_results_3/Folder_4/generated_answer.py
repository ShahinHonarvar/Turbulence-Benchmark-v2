def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = 0
    a = 0
    b = 1
    for _ in range(118):
        fibonacci = a + b
        a = b
        b = fibonacci
    return decimal % fibonacci == 0