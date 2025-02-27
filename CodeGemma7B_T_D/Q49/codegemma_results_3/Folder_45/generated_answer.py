def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci_list = [0, 1]
    current_number = 1
    while True:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
        current_number += 1
        if next_number > decimal:
            break
    return decimal % fibonacci_list[28] == 0