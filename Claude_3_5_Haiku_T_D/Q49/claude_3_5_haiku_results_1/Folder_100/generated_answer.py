def if_decimal_is_divisible(binary_str):

    def fibonacci_190th():
        a, b = (0, 1)
        for _ in range(189):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_190th() == 0