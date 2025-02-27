def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_69th = 0
    a = 0
    b = 1
    for _ in range(69):
        a, b = (b, a + b)
        fibonacci_69th = a
    return decimal_number % fibonacci_69th == 0