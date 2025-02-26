def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fib_sequence = [0, 1, 1, 2, 3, 5, 8]
    divisor = fib_sequence[6]
    return decimal_value % divisor == 0