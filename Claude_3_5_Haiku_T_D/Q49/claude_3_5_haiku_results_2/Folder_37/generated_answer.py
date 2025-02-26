def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        decimal = 0
        for i, digit in enumerate(reversed(binary)):
            if digit == '1':
                decimal += 2 ** i
        return decimal
    fib_46 = fibonacci(46)
    decimal_value = binary_to_decimal(binary_string)
    return decimal_value % fib_46 == 0