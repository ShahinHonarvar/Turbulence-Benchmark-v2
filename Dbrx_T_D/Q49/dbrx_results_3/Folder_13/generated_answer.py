def is_fibonacci(number):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(number - (phi ** number - psi ** number) / 5 ** 0.5) < 1e-10

def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    if is_fibonacci(174) and is_fibonacci(decimal_number):
        return decimal_number % int(str(int(is_fibonacci(174)) * 10 ** len(bin(decimal_number)[2:])) / 10) == 0
    return False