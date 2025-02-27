def if_decimal_is_divisible(binary_representation):
    binary_to_decimal = int(binary_representation, 2)
    fibonacci_list = [0, 1]
    for i in range(2, 100):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    for i in fibonacci_list:
        if i % 6 == 0 and i >= binary_to_decimal:
            if i == binary_to_decimal:
                return True
    return False