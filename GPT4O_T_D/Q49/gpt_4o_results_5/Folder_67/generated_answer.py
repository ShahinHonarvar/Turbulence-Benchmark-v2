def if_decimal_is_divisible(binary_string):
    fib_107th = 12586269025
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_107th == 0