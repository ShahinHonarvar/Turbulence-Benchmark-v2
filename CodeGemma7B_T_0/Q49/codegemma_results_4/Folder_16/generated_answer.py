def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        if n == 0:
            return fibonacci(n)
        else:
            return fibonacci(n - 1)

    def get_decimal_value(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal
    nth_fibonacci = get_nth_fibonacci(get_decimal_value(binary))
    return nth_fibonacci % 128 == 0