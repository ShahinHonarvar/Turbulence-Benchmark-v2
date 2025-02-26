def if_decimal_is_divisible(binary_str):

    def fibonacci_109():
        a, b = (0, 1)
        for _ in range(108):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_109 = fibonacci_109()
    return decimal_num % fib_109 == 0