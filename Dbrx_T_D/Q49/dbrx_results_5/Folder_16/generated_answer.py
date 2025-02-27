def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_list = [0, 1]
    for i in range(128 - 2):
        fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i + 1])
    fibonacci_number = fibonacci_list[127]
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False