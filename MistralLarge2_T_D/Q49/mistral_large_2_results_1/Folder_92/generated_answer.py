def if_decimal_is_divisible(binary):
    fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13]
    decimal = int(binary, 2)
    return decimal % fib_numbers[7] == 0