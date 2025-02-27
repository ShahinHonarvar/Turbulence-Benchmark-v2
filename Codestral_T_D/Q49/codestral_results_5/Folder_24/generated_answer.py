def if_decimal_is_divisible(binary_str):

    def fibo(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    return decimal % fibo(56) == 0