def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_59th_number = 927372692193078999176
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_59th_number == 0