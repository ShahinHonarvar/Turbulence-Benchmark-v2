def if_decimal_is_divisible(binary_representation):
    decimal_value = int(binary_representation, 2)
    fibonacci_list = [0, 1]
    for i in range(2, 87 + 1):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    fibonacci_87th = fibonacci_list[86]
    return decimal_value % fibonacci_87th == 0