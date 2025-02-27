def if_decimal_is_divisible(binary_string):
    fibo_19 = 0
    a, b = (0, 1)
    for _ in range(19):
        fibo_19, a, b = (b, b, a + b)
    decimal = int(binary_string, 2)
    return decimal % fibo_19 == 0