def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_110th = 573147844013817084101
    return decimal_number % fibonacci_110th == 0