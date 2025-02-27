def if_decimal_is_divisible(binary_representation):

    def fibonacci(number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return fibonacci(number - 1) + fibonacci(number - 2)
    decimal_number = 0
    for digit in binary_representation:
        decimal_number = decimal_number * 2 + int(digit)
    index = 0
    current_fibonacci_number = fibonacci(index)
    while decimal_number >= current_fibonacci_number:
        if decimal_number % current_fibonacci_number == 0:
            return True
        index += 1
        current_fibonacci_number = fibonacci(index)
    return False