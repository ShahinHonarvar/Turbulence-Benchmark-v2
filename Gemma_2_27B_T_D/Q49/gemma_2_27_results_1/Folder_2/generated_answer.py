def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_125 = 3219516967710967388521873
    return decimal_value % fibonacci_125 == 0