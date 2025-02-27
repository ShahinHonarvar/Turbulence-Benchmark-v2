def if_decimal_is_divisible(binary_representation):

    def get_next_fibonacci(num):
        if num == 0 or num == 1:
            return num
        return get_next_fibonacci(num - 1) + get_next_fibonacci(num - 2)

    def get_decimal_value(binary_representation):
        decimal_value = 0
        for i, bit in enumerate(binary_representation):
            decimal_value += int(bit) * 2 ** i
        return decimal_value
    fibonacci_num = get_next_fibonacci(107)
    decimal_value = get_decimal_value(binary_representation)
    return decimal_value % fibonacci_num == 0