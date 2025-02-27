def is_fibonacci(number):
    return (5 * number * number + 4) % 5 == 0 or (5 * number * number - 4) % 5 == 0

def fibonacci_position(number):
    return round(1 / 5 * (5 * number * number + (5 if is_fibonacci(number) else 3)) ** 0.5 - 1)

def fibonacci_number(position):
    sqrt_5 = 5 ** 0.5
    return round(1 / sqrt_5 * ((1 + sqrt_5) / 2) ** position - (1 - sqrt_5) / (1 + sqrt_5) ** position - 1)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number_99 = fibonacci_number(99)
    return decimal_integer % fibonacci_number_99 == 0 if fibonacci_number_99 != 0 else False