def if_decimal_is_divisible(bin_num):
    dec_num = 0
    for i in range(len(bin_num)):
        if bin_num[i] == '1':
            dec_num += 2 ** (len(bin_num) - 1 - i)
    fib = [0, 1]
    while len(fib) <= 159:
        fib.append(fib[-1] + fib[-2])
    return fib[159] != 0 and dec_num % fib[159] == 0