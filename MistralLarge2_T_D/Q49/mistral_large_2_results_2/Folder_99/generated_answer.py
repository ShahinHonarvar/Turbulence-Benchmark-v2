def if_decimal_is_divisible(binary_str):

    def nth_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    fibonacci_109 = nth_fibonacci(109)
    return decimal_value % fibonacci_109 == 0