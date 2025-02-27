def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci_64th = 10610209857723
    return decimal_value % fibonacci_64th == 0