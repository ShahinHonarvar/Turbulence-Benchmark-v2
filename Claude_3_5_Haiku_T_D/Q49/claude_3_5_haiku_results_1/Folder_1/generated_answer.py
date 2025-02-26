def if_decimal_is_divisible(binary_str):

    def get_90th_fibonacci():
        a, b = (0, 1)
        for _ in range(89):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_90 = get_90th_fibonacci()
    return decimal_num % fib_90 == 0