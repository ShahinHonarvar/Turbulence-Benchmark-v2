def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_199th = 198412033483787209239547504984829550101091791993016290666627301
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_199th == 0