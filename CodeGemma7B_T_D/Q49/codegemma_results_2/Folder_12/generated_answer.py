def if_decimal_is_divisible(binary_string):
    fibonacci_list = [0, 1]
    index = 2
    while fibonacci_list[-1] <= 66:
        fibonacci_list.append(fibonacci_list[index - 1] + fibonacci_list[index - 2])
        index += 1
    if int(binary_string, 2) % fibonacci_list[fibonacci_list.index(66)] == 0:
        return True
    else:
        return False