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
    decimal_number = binary_to_decimal(binary_str)
    fib109 = fibonacci(109)
    return decimal_number % fib109 == 0