def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_99th_number = 2111485077978050
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_99th_number == 0