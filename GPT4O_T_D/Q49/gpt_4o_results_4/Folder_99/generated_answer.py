def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_109th = 4953053512425937026496
    return decimal_number % fib_109th == 0