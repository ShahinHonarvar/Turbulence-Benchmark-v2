def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_189th = 188927887197340836185700524597912492126
    binary_int = int(binary_str, 2)
    return binary_int % fib_189th == 0