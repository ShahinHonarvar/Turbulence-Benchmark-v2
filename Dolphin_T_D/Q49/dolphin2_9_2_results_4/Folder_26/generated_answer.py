def if_decimal_is_divisible(binary_string):

    def binary_to_decimal(binary_string):
        return int(binary_string, 2)

    def is_fibonacci_138_divisible(n):
        fib_138 = fibonacci(138)
        if fib_138 != 0:
            return n % fib_138 == 0
        else:
            return False

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    dec_num = binary_to_decimal(binary_string)
    return is_fibonacci_138_divisible(dec_num)