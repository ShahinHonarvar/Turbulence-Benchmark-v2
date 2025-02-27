def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_160th_number = 2226687726339736700918011384170852930263733097446731103312089904121
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_160th_number == 0