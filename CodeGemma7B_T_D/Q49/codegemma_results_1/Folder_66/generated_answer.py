def fibonacci(n):
    a, b = (0, 1)
    for i in range(n):
        a, b = (b, a + b)
    return a

def is_divisible(binary):
    decimal = int(binary, 2)
    i = 0
    while fibonacci(i) <= decimal:
        i += 1
    return fibonacci(i) % 120 == 0