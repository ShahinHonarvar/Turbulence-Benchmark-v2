def if_decimal_is_divisible(binary_str):

    def fibonacci_ninth_number():
        a, b = (0, 1)
        for _ in range(8):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    ninth_fib = fibonacci_ninth_number()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % ninth_fib == 0