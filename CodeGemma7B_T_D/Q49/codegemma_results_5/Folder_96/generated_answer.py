def if_decimal_is_divisible(binary_string):

    def fibonacci_47th():
        a, b = (0, 1)
        num = 2
        while num <= 47:
            a, b = (b, a + b)
            num += 1
        return b
    if int(binary_string, 2) % fibonacci_47th() == 0:
        return True
    return False