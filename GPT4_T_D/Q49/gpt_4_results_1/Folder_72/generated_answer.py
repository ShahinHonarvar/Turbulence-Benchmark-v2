def fibonacci(n):
    sequence = []
    a, b = (0, 1)
    while len(sequence) < n:
        sequence.append(a)
        a, b = (b, a + b)
    return sequence[-1]

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_175 = fibonacci(176)
    return decimal % fib_175 == 0