def if_decimal_is_divisible(bin_str):
    fibonacci_76 = 51680708854858323072
    decimal_value = int(bin_str, 2)
    return decimal_value % fibonacci_76 == 0