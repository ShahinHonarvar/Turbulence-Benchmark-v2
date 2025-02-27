def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / 5 ** 0.5) < 1e-10

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    if decimal % fibonacci(166) == 0:
        return True
    else:
        return False