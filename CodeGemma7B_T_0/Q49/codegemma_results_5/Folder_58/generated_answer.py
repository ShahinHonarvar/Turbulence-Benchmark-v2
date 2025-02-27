def if_decimal_is_divisible(binary_representation):

    def get_fibonacci(index):
        if index == 0:
            return 0
        elif index == 1:
            return 1
        else:
            return get_fibonacci(index - 1) + get_fibonacci(index - 2)

    def get_decimal_value(binary_representation):
        decimal_value = 0
        for i, bit in enumerate(binary_representation):
            decimal_value += int(bit) * 2 ** i
        return decimal_value
    fibonacci_value = get_fibonacci(get_decimal_value(binary_representation) // 105)
    return fibonacci_value % 105 == 0