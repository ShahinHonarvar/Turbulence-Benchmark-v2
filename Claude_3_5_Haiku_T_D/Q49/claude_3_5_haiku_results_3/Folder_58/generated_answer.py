def if_decimal_is_divisible(binary_str):

    def fib_105():
        a, b = (0, 1)
        for _ in range(104):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_105_number = fib_105()
    decimal_number = binary_to_decimal(binary_str)
    return decimal_number % fib_105_number == 0