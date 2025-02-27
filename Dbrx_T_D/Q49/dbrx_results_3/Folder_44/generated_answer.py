def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs((phi ** n - psi ** n) / 5 ** 0.5) < 1e-10

def bin_to_decimal(bin_str):
    return sum((int(bit) * 2 ** i for i, bit in enumerate(reversed(bin_str))))

def if_decimal_is_divisible(bin_str):
    decimal = bin_to_decimal(bin_str)
    fib_num = next(filter(is_fibonacci, count(0)), None)
    while fib_num is not None and fib_num < decimal:
        fib_num = next(filter(is_fibonacci, count(fib_num + 1)), None)
    return decimal % fib_num == 0