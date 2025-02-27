def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)

    def fibonacci_sequence():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    for number in fibonacci_sequence():
        if number == 115:
            break
    if decimal_integer % number == 0:
        return True
    else:
        return False