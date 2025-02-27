def if_decimal_is_divisible(binary_str):
    fibonacci_48th = 4807526976
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_48th == 0