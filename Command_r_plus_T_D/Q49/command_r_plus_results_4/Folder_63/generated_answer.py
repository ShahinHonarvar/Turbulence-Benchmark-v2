def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_144 = 12200160415121876738
    binary_int = int(binary_str, 2)
    return binary_int % fib_144 == 0