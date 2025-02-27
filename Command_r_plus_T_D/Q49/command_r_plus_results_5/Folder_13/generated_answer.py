def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_174th_number = 10610209857723
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_174th_number == 0