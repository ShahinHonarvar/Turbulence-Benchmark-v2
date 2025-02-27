def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_59th_number = 927372692193078999176
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_59th_number == 0