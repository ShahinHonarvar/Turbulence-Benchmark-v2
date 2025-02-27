def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_78th = [0, 1]
    i = 2
    while i < 78:
        fib_78th.append(fib_78th[i - 1] + fib_78th[i - 2])
        i += 1
    return decimal_num % fib_78th[77] == 0