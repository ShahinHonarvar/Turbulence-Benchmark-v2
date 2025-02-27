def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_num % fibonacci(127) == 0