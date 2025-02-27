def if_decimal_is_divisible(binary_str):

    def get_fibonacci(n):
        if n <= 1:
            return n
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)

    def get_binary_decimal(binary_str):
        decimal = 0
        for i, bit in enumerate(binary_str):
            decimal += int(bit) * 2 ** i
        return decimal
    fibonacci_185 = get_fibonacci(185)
    decimal = get_binary_decimal(binary_str)
    return decimal % fibonacci_185 == 0