def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_100th_number = 354224848179261915075
    binary_as_decimal = int(binary_str, 2)
    return binary_as_decimal % fib_100th_number == 0