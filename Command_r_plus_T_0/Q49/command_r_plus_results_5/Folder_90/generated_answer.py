def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_177th_number = 15356430217054171130982842882190
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_177th_number == 0