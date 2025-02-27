def is_fibonacci(n):

    def is_valid(number):
        return number == 0 or number == 1 or (number % 2 == 1 and is_fibonacci(number // 2))
    if n == 0 or n == 1:
        return True
    elif n % 2 == 0:
        return False
    else:
        return is_valid(n - (5 ** ((n - 1) // 2) - (-1) ** ((n - 1) // 2)) // 2)

def to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_representation):
    decimal_number = to_decimal(binary_representation)
    fibonacci_number = 159
    while fibonacci_number <= decimal_number:
        fibonacci_number = fibonacci_number * 100 + 159
    return decimal_number % fibonacci_number == 0