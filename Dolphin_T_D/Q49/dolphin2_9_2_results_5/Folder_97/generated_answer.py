def if_decimal_is_divisible(binary_num):

    def fibonacci(n):
        a, b = (0, 1)
        while n:
            a, b = (b, a + b)
            n -= 1
        return a
    n = int(binary_num, 2)
    return n % fibonacci(114) == 0