def if_decimal_is_divisible(bin_str):
    fib_list = [0, 1]
    n = 0
    while fib_list[n] <= int(bin_str, 2):
        fib_list.append(fib_list[n] + fib_list[n + 1])
        n += 1
    return int(bin_str, 2) % fib_list[44] == 0