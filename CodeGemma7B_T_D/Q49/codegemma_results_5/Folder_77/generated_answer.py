def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_value(binary):
        return int(binary, 2)

    def fibonacci_index(limit):
        current, n = (0, 0)
        while current < limit:
            current = fibonacci(n)
            n += 1
        return n - 1
    nth_fibonacci_number = fibonacci(fibonacci_index(decimal_value(binary_representation)))
    return decimal_value(binary_representation) % nth_fibonacci_number == 0