def if_decimal_is_divisible(f: str):

    def nth_fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

    def get_110th_fibonacci():
        n = 0
        while nth_fibonacci(n) < 110:
            n += 1
        return nth_fibonacci(n)
    decimal_value = 0
    for digit in f:
        decimal_value = decimal_value * 2 + int(digit)
    return decimal_value % get_110th_fibonacci() == 0