def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 35):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    thirty_fourth_number = fibonacci_seq[34]
    if decimal_number % thirty_fourth_number == 0:
        return True
    else:
        return False