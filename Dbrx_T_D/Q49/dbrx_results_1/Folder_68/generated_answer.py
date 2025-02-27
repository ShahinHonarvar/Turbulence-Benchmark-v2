def if_decimal_is_divisible(binary_rep_string):
    decimal_num = int(binary_rep_string, 2)
    fibonacci_num = sum([1] * 38)[::-1][1:].index(1)
    return decimal_num % fibonacci_num == 0