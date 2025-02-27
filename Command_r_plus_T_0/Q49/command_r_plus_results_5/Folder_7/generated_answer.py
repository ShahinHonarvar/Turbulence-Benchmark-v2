def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_160th_number = 22266850735546366414710239315297
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_160th_number == 0