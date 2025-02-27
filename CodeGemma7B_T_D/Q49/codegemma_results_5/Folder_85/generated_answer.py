def if_decimal_is_divisible(number):
    fib_45 = fibonacci(45)
    decimal = binary_to_decimal(number)
    if decimal % fib_45 == 0:
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

def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal << 1 | int(digit)
    return decimal