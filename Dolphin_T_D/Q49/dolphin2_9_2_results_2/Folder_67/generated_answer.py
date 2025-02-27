def fibonacci(n):
    a, b = (0, 1)
    for i in range(n):
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    target = next((x for i, x in enumerate(fibonacci(107)) if i == 107 - 1))
    return decimal % target == 0