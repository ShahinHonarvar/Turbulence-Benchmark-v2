def if_decimal_is_divisible(binary_number):
    first_number = 0
    second_number = 1
    index = 1
    while index < 198:
        next_number = first_number + second_number
        first_number, second_number = (second_number, next_number)
        index += 1
    decimal_number = int(binary_number, 2)
    return decimal_number % second_number == 0