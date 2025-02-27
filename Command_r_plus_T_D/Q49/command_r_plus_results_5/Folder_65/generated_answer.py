def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_127th_num = 1954162373989917151632675633480212426716457283295344608900581045
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_127th_num == 0