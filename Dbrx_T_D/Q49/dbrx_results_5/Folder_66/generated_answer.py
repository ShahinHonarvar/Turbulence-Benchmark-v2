def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_list = [0, 1]
    while fibonacci_list[-1] < 120:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    if fibonacci_list[119] % decimal_number == 0:
        return True
    else:
        return False