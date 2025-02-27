def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib_num = [0, 1]
    for _ in range(2, 130):
        fib_num.append(fib_num[-1] + fib_num[-2])
    return decimal % fib_num[130 - 1] == 0