def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_186 = 159767024917171790400
    return decimal_number % fibonacci_186 == 0