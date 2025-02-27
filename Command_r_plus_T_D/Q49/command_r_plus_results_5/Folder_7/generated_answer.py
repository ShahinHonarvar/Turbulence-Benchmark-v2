def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_160th_number = 130797921816447422493144856780886787017151713712709103127
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_160th_number == 0