def if_decimal_is_divisible(binary_string):

    def get_fibonacci_number(n):
        a = 0
        b = 1
        for i in range(n):
            a, b = (b, a + b)
        return a
    n = 190
    decimal_representation = int(binary_string, 2)
    fibonacci_number = get_fibonacci_number(n)
    if decimal_representation % fibonacci_number == 0:
        return True
    else:
        return False