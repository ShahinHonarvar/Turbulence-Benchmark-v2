def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    return decimal_num % fibonacci_numbers[3] == 0