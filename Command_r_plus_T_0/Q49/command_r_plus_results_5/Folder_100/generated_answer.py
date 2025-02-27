def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_190th = 2226606553498079919622709493897993840499
    decimal = int(binary_str, 2)
    return decimal % fib_190th == 0