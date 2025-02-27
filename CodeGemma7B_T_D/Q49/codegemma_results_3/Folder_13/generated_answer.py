def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = 0
    for i in range(1, 175):
        fibonacci_number += fibonacci_number
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False