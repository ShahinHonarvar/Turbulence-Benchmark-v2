def if_decimal_is_divisible(binary_str):

    def fibonacci_64():
        a, b = (0, 1)
        for _ in range(63):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    decimal_num = binary_to_decimal(binary_str)
    fib_64 = fibonacci_64()
    return decimal_num % fib_64 == 0