def if_decimal_is_divisible(binary_representation):
    sum = 0
    counter = 0
    for digit in reversed(binary_representation):
        sum += 2 ** counter * int(digit)
        counter += 1
    value_to_check = sum
    while value_to_check % 2 == 0:
        value_to_check //= 2
    fibonacci_counter = 2
    while value_to_check != 1:
        fibonacci_counter += 1
        if fibonacci_counter % 2 == 0:
            continue
        previous_value = 0
        current_value = 1
        for _ in range(fibonacci_counter):
            previous_value, current_value = (current_value, previous_value + current_value)
        value_to_check -= current_value
        if value_to_check < current_value:
            return False
    return True