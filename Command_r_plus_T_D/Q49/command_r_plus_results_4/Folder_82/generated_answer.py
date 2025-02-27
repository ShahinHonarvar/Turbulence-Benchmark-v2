def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_99th_num = 2111485077978050
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_99th_num == 0