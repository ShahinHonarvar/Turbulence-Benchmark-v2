from math import sqrt

def if_decimal_is_divisible(binary_representation):
    current_number = 0
    i = int(sqrt(len(binary_representation)))
    if len(binary_representation) % 2 == 0:
        i -= 1
    for digit in binary_representation[:i + 1][::-1]:
        current_number += int(digit) * 2 ** i
        i -= 1
    for digit in binary_representation[i + 1:][::-1]:
        current_number += int(digit) * 2 ** (len(binary_representation) - i - 2)
        i -= 1
    return current_number % fibonacci(109) == 0

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)