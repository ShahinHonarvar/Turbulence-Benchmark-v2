def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_174th_number = 1134903170
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_174th_number == 0