def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_147 = 7540113804746346429
    return decimal_value % fibonacci_147 == 0