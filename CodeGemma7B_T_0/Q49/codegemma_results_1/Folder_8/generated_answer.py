def if_decimal_is_divisible(binary_str):

    def get_fib_num(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return get_fib_num(n - 1) + get_fib_num(n - 2)

    def get_decimal_value(binary_str):
        decimal_value = 0
        for i, bit in enumerate(binary_str):
            decimal_value += int(bit) * 2 ** i
        return decimal_value
    fib_num = get_fib_num(54)
    decimal_value = get_decimal_value(binary_str)
    return decimal_value % fib_num == 0