def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 1e-10

def fib_index(n):
    i = 0
    while True:
        if is_fibonacci(i) and int(n) == int((phi ** i - psi ** i) / (phi - psi)):
            return i
        i += 1

def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib_num = fibonacci(fib_index(decimal))
    return decimal % fib_num == 0

def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, n):
            a, b = (b, a + b)
        return b