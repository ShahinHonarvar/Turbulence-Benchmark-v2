import math

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    sqrt_5 = math.sqrt(5)
    fib_135 = int((phi ** 135 - psi ** 135) / sqrt_5)
    return decimal_num % fib_135 == 0