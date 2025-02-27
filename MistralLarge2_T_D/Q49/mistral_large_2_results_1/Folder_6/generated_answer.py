def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_185 = 2111485077978050
    return decimal_number % fibonacci_185 == 0