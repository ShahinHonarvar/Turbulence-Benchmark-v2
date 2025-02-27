def if_decimal_is_divisible(binary_string):

    def is_divisible_by_fib(n):
        a, b = (0, 1)
        for i in range(2, n + 1):
            a, b = (b, a + b)
        return n % b == 0
    decimal_value = int(binary_string, 2)
    return is_divisible_by_fib(decimal_value)