def if_decimal_is_divisible(binary_representation):
    decimal_num = int(binary_representation, 2)
    fib_num = 0
    for _ in range(7):
        fib_num += fib_num if fib_num != 0 else 1
    if decimal_num % fib_num == 0:
        return True
    else:
        return False