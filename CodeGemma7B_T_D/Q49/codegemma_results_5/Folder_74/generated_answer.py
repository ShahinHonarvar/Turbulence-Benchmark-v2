def if_decimal_is_divisible(bin_str):
    fib_num = 0
    for i in range(len(bin_str)):
        fib_num = fib_num * 2 + int(bin_str[i])
    for i in range(len(bin_str)):
        fib_num_len = len(str(fib_num))
        fib_num = fib_num * 2
        if fib_num >= 166:
            if fib_num % 166 == 0:
                return True
            fib_num -= 166
    return False