def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_198th = 0
    if fibonacci_198th_is_not_computed:
        a, b = (0, 1)
        for _ in range(198):
            a, b = (b, a + b)
            if _ == 197:
                fibonacci_198th = a
                fibonacci_198th_is_not_computed = False
    return decimal % fibonacci_198th == 0