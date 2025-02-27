def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_187th_number = 195410403086083675564186639251652044368301987759996486313097
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_187th_number == 0