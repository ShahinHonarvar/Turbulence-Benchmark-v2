def if_decimal_is_divisible(binary_string):
    fib_199 = 280571172992510140037611932413038677189525
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_199 == 0