def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_74th_number = 1134903170
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_74th_number == 0