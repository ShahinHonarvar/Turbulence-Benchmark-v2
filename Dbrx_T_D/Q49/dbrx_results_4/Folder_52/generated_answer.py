def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 1e-10

def fib():
    num, prev_num = (0, 1)
    while True:
        yield num
        num, prev_num = (num + prev_num, num)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if not is_fibonacci(decimal_integer):
        return False
    fibonacci_sequence = fib()
    for _ in range(176):
        fibonacci_number = next(fibonacci_sequence)
    return decimal_integer % fibonacci_number == 0