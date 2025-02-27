def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_59th_number = 9227465
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_59th_number == 0