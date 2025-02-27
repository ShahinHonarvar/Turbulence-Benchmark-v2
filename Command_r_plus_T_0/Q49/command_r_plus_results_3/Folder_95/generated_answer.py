def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_168 = 1688010428570229978767294819069290179922239221908510423453076027503198496149
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_168 == 0