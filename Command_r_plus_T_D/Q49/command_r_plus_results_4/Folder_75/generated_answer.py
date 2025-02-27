def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_189th_num = 235029105667397777445011204280867056793
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_189th_num == 0