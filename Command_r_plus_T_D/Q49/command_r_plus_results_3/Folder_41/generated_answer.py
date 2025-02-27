def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_67th_number = 186514807030480582124375297043687306073014790971745587493
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_67th_number == 0