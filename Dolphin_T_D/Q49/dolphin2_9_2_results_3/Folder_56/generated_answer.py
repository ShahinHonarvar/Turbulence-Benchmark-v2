def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    fibonacci_number = 0
    a, b = (0, 1)
    for i in range(84):
        fibonacci_number = a
        a, b = (b, a + b)
    return n % fibonacci_number == 0