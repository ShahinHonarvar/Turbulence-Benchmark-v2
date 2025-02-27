def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_56 = 106194190191002114555111983882129699246786552976903865104415221473
    return decimal_value % fibonacci_56 == 0