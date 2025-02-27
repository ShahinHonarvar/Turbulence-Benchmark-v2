def if_decimal_is_divisible(bin_num):
    num = int(bin_num, 2)
    a = b = 0
    count = 0
    while count < 60:
        if count < 2:
            fib = count
        else:
            fib = a + b
            a, b = (b, fib)
        if count == 59:
            return num % fib == 0
        count += 1