def is_decimal_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_num = 0
    count = 0
    while count < 145:
        next_fibonacci_num = fibonacci_num + 1
        fibonacci_num = next_fibonacci_num
        count += 1
    if fibonacci_num == 0:
        return False
    if decimal_integer % fibonacci_num == 0:
        return True
    else:
        return False