def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fib_146 = fibonacci(145)[1]
    return dec % fib_146 == 0

def fibonacci(n):
    a, b = (0, 1)
    for i in range(n):
        a, b = (b, a + b)
    return (a, b)