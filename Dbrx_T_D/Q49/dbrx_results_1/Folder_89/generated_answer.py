def is_decimal_divisible_by_126th_fibonacci(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_126 = sum([pow(2, i) for i in range(126)])
    return decimal_integer % fibonacci_126 == 0