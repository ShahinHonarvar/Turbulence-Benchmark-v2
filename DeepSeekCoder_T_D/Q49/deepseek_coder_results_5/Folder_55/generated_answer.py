def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary_str):
        decimal = 0
        for digit in binary_str:
            decimal = decimal * 2 + int(digit)
        return decimal

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_value = binary_to_decimal(binary_str)
    fib_39 = fibonacci(39)
    return decimal_value % fib_39 == 0