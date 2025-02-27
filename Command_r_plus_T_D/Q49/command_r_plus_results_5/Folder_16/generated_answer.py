def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_128th_num = 7540113804746346429
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_128th_num == 0