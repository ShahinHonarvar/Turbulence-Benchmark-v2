def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    fib_n = (phi ** n - psi ** n) / 5 ** 0.5
    return fib_n.is_integer()

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    decimal = binary_to_decimal(binary_str)
    fibonacci_num = 0
    while fibonacci_num < 160:
        fibonacci_num = fibonacci_num + 1
        if is_fibonacci(fibonacci_num) is False:
            continue
        if decimal % fibonacci_num == 0:
            return True
    return False