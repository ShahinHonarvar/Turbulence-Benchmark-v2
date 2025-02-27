def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_154th_number = 29590129428589452733148412967835716481248
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_154th_number == 0