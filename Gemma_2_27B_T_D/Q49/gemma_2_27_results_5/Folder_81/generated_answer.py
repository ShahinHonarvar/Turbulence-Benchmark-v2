def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_97 = 187480657147497167386042888142198
    return decimal_number % fibonacci_97 == 0