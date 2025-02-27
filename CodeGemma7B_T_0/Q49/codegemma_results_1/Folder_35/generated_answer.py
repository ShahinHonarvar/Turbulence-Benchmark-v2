def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        fib_list = [0, 1]
        for i in range(2, n + 1):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list[n]

    def get_decimal_value(binary_str):
        decimal_value = 0
        for i, bit in enumerate(binary_str):
            decimal_value += int(bit) * 2 ** i
        return decimal_value
    nth_fibonacci = get_nth_fibonacci(187)
    decimal_value = get_decimal_value(binary_str)
    return decimal_value % nth_fibonacci == 0