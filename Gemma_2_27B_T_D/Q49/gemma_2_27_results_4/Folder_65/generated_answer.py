def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_number = 0
    a = 0
    b = 1
    for _ in range(127):
        fibonacci_number, a, b = (b, fibonacci_number, fibonacci_number + b)
    return decimal_value % fibonacci_number == 0