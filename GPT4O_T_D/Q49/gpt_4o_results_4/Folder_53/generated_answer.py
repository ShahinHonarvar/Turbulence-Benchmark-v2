def if_decimal_is_divisible(binary_string):
    fib_64th = 10610209857723
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_64th == 0