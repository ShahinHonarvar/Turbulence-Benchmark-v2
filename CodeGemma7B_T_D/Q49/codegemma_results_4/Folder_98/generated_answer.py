def if_decimal_is_divisible(binary_representation):
    fibonacci_index = 14
    decimal_value = int(binary_representation, 2)
    fibonacci_list = [0, 1]
    while len(fibonacci_list) <= fibonacci_index:
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_fibonacci)
    if decimal_value % fibonacci_list[fibonacci_index] == 0:
        return True
    else:
        return False