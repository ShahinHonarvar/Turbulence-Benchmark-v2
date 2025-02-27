def if_decimal_is_divisible(binary_representation):
    fibonacci_list = [0, 1]
    current_number = fibonacci_list[-1]
    for i in range(1, int(binary_representation, 2)):
        current_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(current_number)
    if current_number % int(binary_representation, 2) == 0:
        return True
    else:
        return False