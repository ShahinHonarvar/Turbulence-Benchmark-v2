def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary_str):
        decimal_number = 0
        for digit in binary_str:
            decimal_number = decimal_number * 2 + int(digit)
        return decimal_number

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_number = binary_to_decimal(binary_str)
    fib_97 = fibonacci(97)
    return decimal_number % fib_97 == 0