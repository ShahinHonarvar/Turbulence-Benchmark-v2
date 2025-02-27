def if_decimal_is_divisible(binary):

    def get_fibo_at(n):
        a, b = (0, 1)
        while n:
            a, b = (b, a + b)
            n -= 1
        return a

    def binary_to_decim(binary):
        return int(binary, 2)
    fibo_54 = get_fibo_at(54)
    decim = binary_to_decim(binary)
    return decim % fibo_54 == 0