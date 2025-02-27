from sympy import fibonacci

def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_number_150 = fibonacci(150)
    return decimal_number % fibonacci_number_150 == 0