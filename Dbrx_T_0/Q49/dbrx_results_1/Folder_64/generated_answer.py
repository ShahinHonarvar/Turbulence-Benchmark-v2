def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 34
    while fibonacci_number < decimal_number:
        fibonacci_number = int(((1 + 5 ** 0.5) / 2) ** fibonacci_number - ((1 - 5 ** 0.5) / 2) ** fibonacci_number) // 5
    return decimal_number % fibonacci_number == 0