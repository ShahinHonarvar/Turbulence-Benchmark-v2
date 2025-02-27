def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_198th = 946917780233746805048858157684235075729102132941066729
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_198th == 0