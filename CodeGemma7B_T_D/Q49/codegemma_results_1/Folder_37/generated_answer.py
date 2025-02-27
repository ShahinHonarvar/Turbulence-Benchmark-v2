def if_decimal_is_divisible(binary_string):
    fibonacci_values = [0, 1]
    while fibonacci_values[-1] < 46:
        fibonacci_values.append(fibonacci_values[-1] + fibonacci_values[-2])
    decimal_value = int(binary_string, 2)
    if decimal_value % fibonacci_values[45] == 0:
        return True
    else:
        return False