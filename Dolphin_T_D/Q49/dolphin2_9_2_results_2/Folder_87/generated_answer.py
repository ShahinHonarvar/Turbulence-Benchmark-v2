def if_decimal_is_divisible(binary_str):

    def dec_to_bin(n):
        if n == 0:
            return '0'
        bin_str = ''
        while n > 0:
            bin_str = ('1' if n % 2 == 1 else '0') + bin_str
            n = n // 2
        return bin_str
    i = 0
    fib_180 = fib_prev = 0
    fib_curr = 1
    while i < 180:
        fib_180 = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_180
        i += 1
    dec_num = int(binary_str, 2)
    return dec_num % fib_180 == 0