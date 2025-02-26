def if_decimal_is_divisible(binary_string):

    def fibonacci_105th():
        if not hasattr(fibonacci_105th, 'value'):
            a, b = (0, 1)
            for _ in range(104):
                a, b = (b, a + b)
            fibonacci_105th.value = b
        return fibonacci_105th.value
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_105th() == 0