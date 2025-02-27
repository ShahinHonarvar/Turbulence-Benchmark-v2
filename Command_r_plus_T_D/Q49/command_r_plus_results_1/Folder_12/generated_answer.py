def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_66th_num = 121393
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_66th_num == 0