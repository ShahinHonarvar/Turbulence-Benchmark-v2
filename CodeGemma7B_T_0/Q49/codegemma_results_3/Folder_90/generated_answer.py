def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        if n < 1:
            return None
        return fibonacci(n - 1)

    def get_decimal_value(binary):
        return int(binary, 2)
    nth_fibonacci = get_nth_fibonacci(177)
    if nth_fibonacci is None:
        return False
    return get_decimal_value(binary) % nth_fibonacci == 0