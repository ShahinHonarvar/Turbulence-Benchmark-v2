def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    first, second = (0, 1)
    fib_number = 1
    while fib_number < 48:
        first, second = (second, first + second)
        fib_number += 1
    return decimal % second == 0