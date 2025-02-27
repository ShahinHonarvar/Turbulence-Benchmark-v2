def if_decimal_is_divisible(bin_str):
    decimal_int = int(bin_str, 2)
    fib_list = [0, 1]
    n = 2
    while fib_list[-1] < decimal_int:
        fib_list.append(fib_list[n - 1] + fib_list[n - 2])
        n += 1
    if decimal_int % fib_list[136] == 0:
        return True
    return False