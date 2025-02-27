def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal

    def is_divisible(number, divisor):
        return number % divisor == 0
    decimal = binary_to_decimal(binary)
    for i in range(74):
        if is_divisible(decimal, fibonacci(i)):
            return True
    return False