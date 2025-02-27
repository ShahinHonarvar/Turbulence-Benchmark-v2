def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_199 = 96045837124262269495886494721171213
    return decimal_number % fibonacci_199 == 0