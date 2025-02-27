def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 1e-10

def fibonacci_index(n):
    return round(log(n * (5 ** 0.5 + 1) / 2, 5 ** 0.5) + 0.5)

def is_decimal_divisible_by_fibonacci(bin_str):
    decimal = int(bin_str, 2)
    fib_number = fibonacci_index(198)
    return decimal % fib_number == 0 if fib_number != 1 else False