def is_fibonacci(number):
    return number >= 0 and number & number - 1 == 0

def fibonacci_nth(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)

def binary_to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_string):
    decimal_number = binary_to_decimal(binary_string)
    if not is_fibonacci(fibonacci_nth((number := 110))):
        raise ValueError('The 110th number in the Fibonacci sequence is not a Fibonacci number.')
    return decimal_number % fibonacci_nth(110) == 0