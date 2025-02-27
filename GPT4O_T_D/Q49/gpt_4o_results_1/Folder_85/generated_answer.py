def if_decimal_is_divisible(binary_str):
    fib_45th = 1134903170
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_45th == 0