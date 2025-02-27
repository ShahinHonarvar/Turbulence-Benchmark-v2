def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_104 = 16021264005686600
    return decimal % fibonacci_104 == 0