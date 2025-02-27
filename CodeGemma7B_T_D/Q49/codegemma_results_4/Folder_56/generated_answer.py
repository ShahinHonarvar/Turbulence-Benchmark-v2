def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    if n % fibonacci(84) == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)