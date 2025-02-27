def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return b

def is_decimal_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_seq = [fibonacci(i) for i in range(171)]
    return decimal % fibonacci_seq[169] == 0