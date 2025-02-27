def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_99th_number = 2111485077978050
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_99th_number == 0