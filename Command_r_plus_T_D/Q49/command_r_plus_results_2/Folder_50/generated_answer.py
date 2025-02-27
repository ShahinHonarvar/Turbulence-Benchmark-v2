def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_119th_number = 19134702400093278051799108472231625
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_119th_number == 0