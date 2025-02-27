def fibonacci(n):
    a, b = (0, 1)
    for i in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_string):
    return fibonacci(66) % int(binary_string, 2) == 0