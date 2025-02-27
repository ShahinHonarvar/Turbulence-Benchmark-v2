def if_decimal_is_divisible(binary):

    def dec_to_bin(n):
        if n == 0:
            return '0'
        num = ''
        while n:
            num = ('1' if n & 1 else '0') + num
            n >>= 1
        return num

    def get_fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    decimal = int(binary, 2)
    fib = get_fibonacci(180)
    return fib != 0 and decimal % fib == 0