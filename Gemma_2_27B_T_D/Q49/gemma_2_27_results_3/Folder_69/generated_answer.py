def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_170 = 10891889195015940781632184795763111857135483656928
    return decimal_value % fibonacci_170 == 0