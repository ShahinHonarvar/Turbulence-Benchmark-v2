def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        for i in range(n):
            yield fibonacci(i)

    def get_binary_decimal(binary_representation):
        return int(binary_representation, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    nth_fibonacci = get_nth_fibonacci(138)
    binary_decimal = get_binary_decimal(binary_representation)
    return is_divisible(next(nth_fibonacci), binary_decimal)