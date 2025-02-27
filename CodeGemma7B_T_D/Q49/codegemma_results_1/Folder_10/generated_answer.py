def if_decimal_is_divisible(binary_representation):
    x = int(binary_representation, 2)
    if x % fibonacci(88) == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)