def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_147 = 122001604151218463608827757749704888773
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_147 == 0