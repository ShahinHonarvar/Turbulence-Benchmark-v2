def if_decimal_is_divisible(binary_str):
    decimal_integer = int(binary_str, 2)
    fibonacci_114 = 619220451666590135228675387863297874269396512
    return decimal_integer % fibonacci_114 == 0