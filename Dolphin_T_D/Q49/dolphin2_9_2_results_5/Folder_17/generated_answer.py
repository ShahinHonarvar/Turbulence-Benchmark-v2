def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    a, b = (0, 1)
    fib_154 = 0
    for _ in range(154):
        a, b = (b, a + b)
        fib_154 = b
    if n % fib_154 == 0:
        return True
    return False