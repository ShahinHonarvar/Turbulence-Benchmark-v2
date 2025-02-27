def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        l, r = [0, 1]
        for _ in range(n):
            l, r = (r, l + r)
        return l
    binary_as_int = int(binary_representation, 2)
    return binary_as_int % fibonacci(87) == 0