def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    a = 0
    b = 1
    for _ in range(154):
        a, b = (b, a + b)
    fib_154 = b
    if decimal_num % fib_154 == 0:
        return True
    else:
        return False