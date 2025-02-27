def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_198th_number = 1989131572813148818330452749886137067901149354010601607728
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_198th_number == 0