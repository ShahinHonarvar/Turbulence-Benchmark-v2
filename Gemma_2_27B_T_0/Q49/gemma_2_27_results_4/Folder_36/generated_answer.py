def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_150 = 99692166771894438081793771788337971717
    return decimal_number % fibonacci_150 == 0