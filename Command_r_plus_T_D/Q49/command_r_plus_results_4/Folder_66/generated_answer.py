def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_120th = 36152819320022200855497297861115574465871533708760951863205519437120898593
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_120th == 0