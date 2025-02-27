def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary_str):
        decimal_value = 0
        for i, bit in enumerate(binary_str):
            decimal_value += int(bit) * 2 ** i
        return decimal_value

    def nth_fibonacci(n):
        if n <= 1:
            return n
        else:
            return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
    decimal_value = binary_to_decimal(binary_str)
    fibonacci_value = nth_fibonacci(60)
    return decimal_value % fibonacci_value == 0