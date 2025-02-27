def if_decimal_is_divisible(bin_str):
    fib_list = [0]
    a, b = (0, 1)
    for i in range(1, 10000):
        fib_list.append(b)
        a, b = (b, a + b)
    decimal_int = int(bin_str, 2)
    while decimal_int > fib_list[-1]:
        fib_list.append(fib_list[-1] + fib_list[-2])
    if decimal_int % fib_list[86] == 0:
        return True
    else:
        return False