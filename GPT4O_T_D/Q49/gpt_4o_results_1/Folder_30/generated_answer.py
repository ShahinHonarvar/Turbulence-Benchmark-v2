def if_decimal_is_divisible(binary_str):
    fib_186 = 8757159534301885445803338634900000000
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_186 == 0