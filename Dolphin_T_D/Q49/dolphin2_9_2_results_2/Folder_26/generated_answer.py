def if_decimal_is_divisible(bin_str):
    dec_num = int(bin_str, 2)
    fib_list = [0, 1]
    a = 0
    b = 1
    for i in range(2, 139):
        a, b = (b, a + b)
        fib_list.append(b)
    fib_138 = fib_list[138]
    if dec_num % fib_138 == 0:
        return True
    else:
        return False