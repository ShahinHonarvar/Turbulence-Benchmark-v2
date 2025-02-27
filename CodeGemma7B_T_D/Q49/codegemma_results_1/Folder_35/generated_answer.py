def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fibonacci_number = 1
    index = 2
    while fibonacci_number < decimal_representation:
        fibonacci_number = fibonacci_number + fibonacci_number
        index += 1
    return index % 187 == 0