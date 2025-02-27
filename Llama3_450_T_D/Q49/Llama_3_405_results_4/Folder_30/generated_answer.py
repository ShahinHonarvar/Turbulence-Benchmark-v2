def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        x, y = (0, 1)
        for _ in range(n):
            x, y = (y, x + y)
        return x
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci(186) == 0