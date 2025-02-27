def if_decimal_is_divisible(binary_number):
    binary_to_decimal = int(binary_number, 2)
    current_number, next_number = (0, 1)
    for _ in range(binary_to_decimal):
        current_number, next_number = (next_number, current_number + next_number)
    if binary_to_decimal % current_number == 0:
        return True
    else:
        return False