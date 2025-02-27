import math

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    fibonacci = int((phi ** 145 - psi ** 145) / sqrt_5)
    return decimal % fibonacci == 0