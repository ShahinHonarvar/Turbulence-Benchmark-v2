def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_64th_number = 184562332962451626378228136326
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_64th_number == 0