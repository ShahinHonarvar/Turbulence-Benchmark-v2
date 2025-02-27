def if_decimal_is_divisible(binary_representation):
    n = 10
    while len(str(fibonacci(n))) < len(binary_representation):
        n += 10
    m = int(binary_representation, 2)
    if m % fibonacci(n) == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = (0, 1)
        for i in range(1, n):
            a, b = (b, a + b)
    return b