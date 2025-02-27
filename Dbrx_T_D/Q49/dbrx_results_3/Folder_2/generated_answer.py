def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def to_decimal(binary_string):
    return int(binary_string, 2)

def is_divisible_by_fibonacci(number):
    fibonacci_numbers = set(fibonacci())
    target_fibonacci_number = 125
    while target_fibonacci_number > 0:
        if number % next(fibonacci_numbers) == 0:
            return True
        target_fibonacci_number -= 1
    return False

def if_decimal_is_divisible(binary_string):
    decimal_number = to_decimal(binary_string)
    return is_divisible_by_fibonacci(decimal_number)