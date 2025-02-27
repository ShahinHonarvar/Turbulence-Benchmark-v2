def if_decimal_is_divisible(binary):

    def get_nth_fibonacci(n):
        a, b = (0, 1)
        for i in range(n):
            a, b = (b, a + b)
        return a
    if int(binary, 2) % get_nth_fibonacci(97) == 0:
        return True
    return False