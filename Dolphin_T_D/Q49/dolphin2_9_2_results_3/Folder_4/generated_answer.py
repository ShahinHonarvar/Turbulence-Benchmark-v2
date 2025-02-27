def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_string):
    m = int(binary_string, 2)
    n = 101
    if fibonacci(n):
        if m % fibonacci(118) == 0:
            return True
        else:
            return False
    else:
        return False