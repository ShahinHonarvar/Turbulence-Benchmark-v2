def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fibonacci_104th = 1429893800835552849
    return decimal_num % fibonacci_104th == 0