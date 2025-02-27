def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < 108:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return decimal % fibonacci_list[107] == 0