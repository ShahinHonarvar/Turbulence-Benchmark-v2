def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    fib_n = int((phi ** n - psi ** n) / 5 ** 0.5)
    return fib_n == n

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_numbers = [i for i in range(10 ** 6) if is_fibonacci(i)]
    return decimal_integer % fibonacci_numbers[178] == 0