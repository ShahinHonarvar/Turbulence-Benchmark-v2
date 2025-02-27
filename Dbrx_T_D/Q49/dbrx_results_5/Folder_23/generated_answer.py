def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 0
    previous_number = -1
    current_number = 0
    count = 0
    while count < 48:
        if fibonacci_number > decimal_number:
            break
        if fibonacci_number == decimal_number:
            return True
        next_number = previous_number + fibonacci_number
        previous_number = fibonacci_number
        fibonacci_number = next_number
        count += 1
    return False