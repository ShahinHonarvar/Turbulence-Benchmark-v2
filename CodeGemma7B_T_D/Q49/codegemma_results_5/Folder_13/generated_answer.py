def if_decimal_is_divisible(binary_representation):
    binary = int(binary_representation, 2)
    fibonacci_index = 2
    a, b = (0, 1)
    while binary >= b:
        a, b = (b, a + b)
        fibonacci_index += 1
    if fibonacci_index % 174 == 0:
        return True
    else:
        return False