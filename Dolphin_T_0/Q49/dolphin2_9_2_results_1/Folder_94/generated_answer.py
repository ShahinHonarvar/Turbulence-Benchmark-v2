def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    fib_40 = fibonacci_sequence[39]
    return fib_40 != 0 and decimal_number % fib_40 == 0