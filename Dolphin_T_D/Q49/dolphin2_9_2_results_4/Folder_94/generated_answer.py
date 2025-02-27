def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 40):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    forty_fibonacci = fibonacci_sequence[39]
    if decimal_integer % forty_fibonacci == 0:
        return True
    else:
        return False