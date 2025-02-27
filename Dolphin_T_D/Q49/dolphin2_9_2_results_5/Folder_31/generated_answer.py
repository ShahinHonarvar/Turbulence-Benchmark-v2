def if_decimal_is_divisible(binary):
    int_value = int(binary, 2)
    fibonacci_69 = [0, 1]
    for i in range(2, 70):
        fibonacci_69.append(fibonacci_69[i - 2] + fibonacci_69[i - 1])
    return int_value % fibonacci_69[-1] == 0