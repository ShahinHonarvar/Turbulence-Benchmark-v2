def if_decimal_is_divisible(binary_representation):

    def get_next_fib(num):
        if num in (0, 1):
            return num
        return get_next_fib(num - 1) + get_next_fib(num - 2)

    def get_decimal_value(binary_representation):
        decimal_value = 0
        for i, bit in enumerate(binary_representation):
            decimal_value += int(bit) * 2 ** i
        return decimal_value
    fib_num = get_next_fib(109)
    return get_decimal_value(binary_representation) % fib_num == 0