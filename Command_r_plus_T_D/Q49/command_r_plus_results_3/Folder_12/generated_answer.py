def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_66th_number = 121393
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_66th_number == 0