def if_decimal_is_divisible(bin_str):
    bin_str_len = len(bin_str)
    list_fib = [0, 1]
    fib_index = 2
    while fib_index < 115:
        fib_size = list_fib[fib_index - 1] + list_fib[fib_index - 2]
        if fib_size > 2 ** bin_str_len:
            break
        else:
            list_fib.append(fib_size)
            fib_index += 1
    if int(bin_str_len % bin_str_len == 0):
        bin_str_reverse = bin_str[::-1]
        power = 0
        for i in range(bin_str_len):
            if bin_str_reverse[i] == '1':
                plus = int(list_fib[power]) % 115
                if plus == 0:
                    return True
            power += 1
    return False