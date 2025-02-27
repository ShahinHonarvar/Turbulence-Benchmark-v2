def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_168 = 1688010428570229970231254932180842278
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_168 == 0