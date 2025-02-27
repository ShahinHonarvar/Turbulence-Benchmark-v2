def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < 164:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    if decimal_number % fibonacci_list[163] == 0:
        return True
    else:
        return False