def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)

    def calc_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_76 = calc_fibonacci(76)
    if decimal % fibonacci_76 == 0:
        return True
    else:
        return False