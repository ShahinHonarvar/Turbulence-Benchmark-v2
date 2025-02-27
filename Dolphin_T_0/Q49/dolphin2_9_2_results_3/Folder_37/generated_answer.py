def if_decimal_is_divisible(binary_representation):
    decimal_value = int(binary_representation, 2)
    fibonacci_target = 0
    fibonacci_1 = 0
    fibonacci_2 = 1
    for _ in range(46):
        fibonacci_target = fibonacci_1 + fibonacci_2
        fibonacci_1 = fibonacci_2
        fibonacci_2 = fibonacci_target
    return decimal_value % fibonacci_target == 0