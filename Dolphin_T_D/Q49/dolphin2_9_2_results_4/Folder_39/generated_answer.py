def fibonacci(n):
    if n < 2:
        return n
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
    return b

def if_decimal_is_divisible(binary_repr):
    decimal = int(binary_repr, 2)
    fibo_15 = fibonacci(15)
    return decimal % fibo_15 == 0