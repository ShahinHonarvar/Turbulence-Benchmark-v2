def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_170th_number = 1908973060461042147070432607469007391381464207837049370714186173023777782022076326626413089
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_170th_number == 0