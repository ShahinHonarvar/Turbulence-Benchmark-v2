def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_64th_number = 184562332962451626378228136326
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_64th_number == 0