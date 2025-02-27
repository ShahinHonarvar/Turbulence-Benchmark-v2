def if_decimal_is_divisible(binary_rep):

    def binary_to_int(binary_rep):
        n = 0
        degrees = len(binary_rep) - 1
        for c in binary_rep:
            if c == '1':
                n += 2 ** degrees
            degrees -= 1
        return n

    def fibonacci(i):
        n = 0
        a = 0
        b = 1
        for _ in range(i):
            n = a
            a = b
            b = n + b
        return n
    return binary_to_int(binary_rep) % fibonacci(108) == 0