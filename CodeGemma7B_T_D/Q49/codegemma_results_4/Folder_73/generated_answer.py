def if_decimal_is_divisible(bi_str):
    fib_num = 0
    fib_i = 0
    k = len(bi_str) - 1
    bi_int = int(bi_str[k], 2)
    while fib_num < 164:
        fact = 2 ** (len(bi_str[1:k]) + 1)
        fib_i += 1
        fib_num = fib_num * 2 + int(bi_str[k - fib_i], 2) * fact
        k -= fib_i + 1
        if fib_num == 164:
            return True
        elif k == -1:
            return False