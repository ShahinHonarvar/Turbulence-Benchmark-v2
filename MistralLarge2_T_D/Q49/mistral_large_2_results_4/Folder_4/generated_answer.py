def fib_n(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_118 = fib_n(118)
    return decimal_num % fib_118 == 0