def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_67th_num = 19070076485965243592395691266028679547389371667000
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_67th_num == 0