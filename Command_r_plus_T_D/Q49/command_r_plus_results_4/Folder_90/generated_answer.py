def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_177th_num = 1514837626707957830984540552430533714832687074345751
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_177th_num == 0