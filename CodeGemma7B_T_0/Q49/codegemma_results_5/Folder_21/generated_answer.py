def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        fib_sequence = [fibonacci(i) for i in range(n + 1)]
        return fib_sequence[n]

    def get_decimal_value(binary_representation):
        decimal_value = 0
        for i, bit in enumerate(binary_representation):
            decimal_value += int(bit) * 2 ** i
        return decimal_value
    nth_fibonacci = get_nth_fibonacci(195)
    decimal_value = get_decimal_value(binary_representation)
    return decimal_value % nth_fibonacci == 0