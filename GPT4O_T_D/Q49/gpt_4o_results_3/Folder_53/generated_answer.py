def if_decimal_is_divisible(binary_str):
    fib_64th = 10610209857723
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_64th == 0