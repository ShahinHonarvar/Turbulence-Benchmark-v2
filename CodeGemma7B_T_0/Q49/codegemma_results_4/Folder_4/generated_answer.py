def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        fib_list = [fibonacci(i) for i in range(n + 1)]
        return fib_list[n]

    def get_decimal_value(binary_str):
        decimal_value = 0
        for i, bit in enumerate(binary_str):
            decimal_value += int(bit) * 2 ** i
        return decimal_value
    nth_fibonacci = get_nth_fibonacci(118)
    decimal_value = get_decimal_value(binary_str)
    return decimal_value % nth_fibonacci == 0