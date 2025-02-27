def if_decimal_is_divisible(binary_string):
    decimal_representation = int(binary_string, 2)
    a = 0
    b = 1
    fibonacci_sequence = [a, b]
    for i in range(2, 13):
        c = a + b
        fibonacci_sequence.append(c)
        a = b
        b = c
    thirteenth_fibonacci_number = fibonacci_sequence[12]
    if decimal_representation % thirteenth_fibonacci_number == 0:
        return True
    else:
        return False