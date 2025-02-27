def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci_list = [0, 1]
    for i in range(2, 196):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    fibonacci = fibonacci_list[-1]
    return decimal % fibonacci == 0