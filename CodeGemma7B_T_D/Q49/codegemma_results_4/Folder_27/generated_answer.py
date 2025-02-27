def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_nminus1 = fibonacci(n - 1)
            fib_nminus2 = fibonacci(n - 2)
            return fib_nminus1 + fib_nminus2

    def binary_to_decimal(binary):
        decimal = 0
        for i, digit in enumerate(binary):
            decimal += int(digit) * 2 ** (len(binary) - i - 1)
        return decimal
    fibonacci_limit = fibonacci(86)
    fibonacci_sequence = [fibonacci(n) for n in range(87)]
    binary_decimal = binary_to_decimal(binary)
    if binary_decimal % fibonacci_sequence[86] == 0:
        return True
    else:
        return False