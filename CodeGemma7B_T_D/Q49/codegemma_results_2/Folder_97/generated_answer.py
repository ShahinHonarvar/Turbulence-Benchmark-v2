def if_decimal_is_divisible(binary_string):
    fibonacci_2 = [0, 1]
    for index in range(2, len(binary_string) + 2):
        fibonacci_2.append(fibonacci_2[index - 1] + fibonacci_2[index - 2])
    return int(binary_string, 2) % fibonacci_2[114] == 0