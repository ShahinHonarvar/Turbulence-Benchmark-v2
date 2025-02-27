def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_174 = 17889033489921027003798431699765322101522066306271866405583958456714190427562873787641
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_174 == 0