def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_118th = 1414275616546690525166021
    decimal = int(binary_str, 2)
    return decimal % fib_118th == 0