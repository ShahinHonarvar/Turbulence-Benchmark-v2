def if_decimal_is_divisible(binary_string):
    processed_string = list(binary_string)
    processed_string.reverse()
    decimal_number = 0
    for index, bit in enumerate(processed_string):
        decimal_number += 2 ** index * int(bit)
    if decimal_number % fibonacci(68) == 0:
        return True
    else:
        return False

def fibonacci(n):
    """Calculates the nth number in the Fibonacci sequence."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)