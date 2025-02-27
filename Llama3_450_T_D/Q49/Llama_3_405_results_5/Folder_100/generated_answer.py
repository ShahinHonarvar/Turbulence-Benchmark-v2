import math

def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        sqrt_5 = math.sqrt(5)
        phi = (1 + sqrt_5) / 2
        return round((phi ** n - (1 - phi) ** n) / sqrt_5)
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci(190) == 0