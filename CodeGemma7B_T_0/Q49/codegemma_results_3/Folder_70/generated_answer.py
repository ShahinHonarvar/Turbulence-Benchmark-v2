def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def get_next_fibonacci(current):
        while True:
            current += 1
            if fibonacci(current) > 137:
                return fibonacci(current)
    decimal = int(binary_str, 2)
    next_fibonacci = get_next_fibonacci(0)
    while True:
        if decimal % next_fibonacci == 0:
            return True
        next_fibonacci = get_next_fibonacci(next_fibonacci)