def is_divisible_by_125th_fibonacci(bin_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_num = int(bin_str, 2)
    return decimal_num % fibonacci(125) == 0