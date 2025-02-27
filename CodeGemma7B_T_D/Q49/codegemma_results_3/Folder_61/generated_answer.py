def if_decimal_is_divisible(binary_representation):

    def get_decimal_value(binary_representation):
        return sum([int(digit) * 2 ** i for i, digit in enumerate(binary_representation)])

    def get_76th_fibonacci_number():
        a, b = (0, 1)
        counter = 0
        while counter < 76:
            a, b = (b, a + b)
            counter += 1
        return a
    return get_decimal_value(binary_representation) % get_76th_fibonacci_number() == 0