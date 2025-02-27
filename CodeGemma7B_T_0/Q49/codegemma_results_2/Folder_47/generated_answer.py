def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        if n < 0:
            return None
        else:
            return fibonacci(n)

    def get_decimal(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_int = get_decimal(binary)
    nth_fibonacci = get_nth_fibonacci(94)
    if is_divisible(binary_int, nth_fibonacci):
        return True
    else:
        return False