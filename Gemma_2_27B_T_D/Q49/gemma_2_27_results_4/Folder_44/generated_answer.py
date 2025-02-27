def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_number = 144
    a = 0
    b = 1
    for i in range(159):
        a, b = (b, a + b)
    return decimal_value % b == 0