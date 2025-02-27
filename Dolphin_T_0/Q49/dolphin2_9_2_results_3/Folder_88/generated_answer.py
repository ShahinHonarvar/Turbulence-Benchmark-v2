def fib_49():
    a, b = (0, 1)
    for _ in range(48):
        a, b = (b, a + b)
    return b

def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    return n % fib_49() == 0