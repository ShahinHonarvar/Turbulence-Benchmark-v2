def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_76th_number = 19009729683
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_76th_number == 0