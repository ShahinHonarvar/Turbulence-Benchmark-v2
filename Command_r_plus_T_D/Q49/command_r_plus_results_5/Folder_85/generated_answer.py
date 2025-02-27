def if_decimal_is_divisible(binary_str):
    fib_45th_num = 1134903170
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_45th_num == 0