def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    fibonacci_list = [0, 1]
    for i in range(2, 68):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    if fibonacci_list[66] != 0 and n % fibonacci_list[66] == 0:
        return True
    else:
        return False