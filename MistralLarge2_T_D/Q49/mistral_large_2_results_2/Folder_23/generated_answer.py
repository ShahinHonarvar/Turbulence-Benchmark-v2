def if_decimal_is_divisible(binary_string):
    fib_48 = 2971215073
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_48 == 0