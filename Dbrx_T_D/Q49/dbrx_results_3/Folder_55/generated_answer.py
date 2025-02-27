def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def nth_fibonacci(n):
    for i, num in enumerate(fibonacci()):
        if i == n:
            return num

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    return decimal_integer % nth_fibonacci(39) == 0