def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 1e-10

def binary_to_decimal(binary_string):
    return int(binary_string, 2)

def fibonacci(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        fib = [0, 1]
        for _ in range(2, position):
            fib.append(fib[-1] + fib[-2])
        return fib[-1]

def if_decimal_is_divisible(binary_representation):
    decimal_number = binary_to_decimal(binary_representation)
    if is_fibonacci(80) and decimal_number % fibonacci(80) == 0:
        return True
    else:
        return False