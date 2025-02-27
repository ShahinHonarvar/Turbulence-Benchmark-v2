def if_decimal_is_divisible(binary_str):

    def get_fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return get_fib(n - 1) + get_fib(n - 2)

    def get_decimal(binary_str):
        decimal = 0
        for i, bit in enumerate(binary_str):
            decimal += int(bit) * 2 ** i
        return decimal
    fib_49 = get_fib(49)
    decimal = get_decimal(binary_str)
    return decimal % fib_49 == 0