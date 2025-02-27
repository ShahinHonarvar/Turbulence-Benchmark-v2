def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_128th_number = 7540113804746346429
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_128th_number == 0