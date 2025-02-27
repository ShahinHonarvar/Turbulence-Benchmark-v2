def if_decimal_is_divisible(binary_str):
    fib_34 = 5702887
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_34 == 0