def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib198 = 1
    a = 0
    b = 1
    for _ in range(197):
        a, b = (b, a + b)
        fib198 = b
    return decimal % fib198 == 0