def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_num = 0
    prev_num = 0
    current_num = 1
    for _ in range(150):
        temp_num = current_num
        current_num += prev_num
        prev_num = temp_num
    fibonacci_num = current_num
    if decimal_integer % fibonacci_num == 0:
        return True
    else:
        return False