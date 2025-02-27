def if_decimal_is_divisible(binary_str):

    def fibonacci_94():
        a, b = (0, 1)
        for _ in range(94):
            a, b = (b, a + b)
        return b
    decimal = int(binary_str, 2)
    return decimal % fibonacci_94() == 0