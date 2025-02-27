def if_decimal_is_divisible(binary):

    def binary_to_decimal(binary):
        decimal, i = (0, 0)
        while binary:
            decimal += int(binary[-1]) * 2 ** i
            binary = binary[:-1]
            i += 1
        return decimal
    decimal = binary_to_decimal(binary)

    def nth_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib28 = nth_fibonacci(28)
    return decimal % fib28 == 0