def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_135th_number = 135 * 2 + 1
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_135th_number == 0