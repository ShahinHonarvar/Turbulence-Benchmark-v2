def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_179th_num = 2226612050148382623074376458410866709718254979
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_179th_num == 0