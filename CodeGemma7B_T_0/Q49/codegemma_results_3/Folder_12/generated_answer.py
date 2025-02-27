def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_next_fibonacci(current):
        next = current
        while True:
            next = fibonacci(next + 1)
            if next > current:
                return next

    def get_decimal(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal

    def is_divisible(number, divisor):
        return number % divisor == 0
    next_fibonacci = get_next_fibonacci(fibonacci(65))
    return is_divisible(get_decimal(binary), next_fibonacci)