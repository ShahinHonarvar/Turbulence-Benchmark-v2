def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 139):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if decimal_value % fibonacci_sequence[137] == 0:
        return True
    else:
        return False