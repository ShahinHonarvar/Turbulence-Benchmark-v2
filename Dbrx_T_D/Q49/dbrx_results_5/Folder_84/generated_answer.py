def is_fibonacci(dividend):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < dividend:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence.index(dividend) % 196 == 0

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    return is_fibonacci(decimal_integer)