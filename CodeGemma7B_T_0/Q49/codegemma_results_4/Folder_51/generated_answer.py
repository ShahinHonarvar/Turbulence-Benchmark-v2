def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_from_binary(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal

    def get_nth_fibonacci(n):
        if n < 0:
            raise ValueError('The Fibonacci sequence is not defined for negative numbers')
        return fibonacci(n - 1)
    binary_int = decimal_from_binary(binary)
    nth_fibonacci = get_nth_fibonacci(17)
    return binary_int % nth_fibonacci == 0