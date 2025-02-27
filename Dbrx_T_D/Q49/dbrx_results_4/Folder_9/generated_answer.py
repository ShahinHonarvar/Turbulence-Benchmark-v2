def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 0.01 * n

def fibonacci_position(n):
    fib, pos = ([0, 1], 0)
    while fib[-1] + fib[-2] < n:
        fib.append(fib[-1] + fib[-2])
        pos += 1
    return pos

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    if not decimal_number % fibonacci_position(68):
        return True
    return False