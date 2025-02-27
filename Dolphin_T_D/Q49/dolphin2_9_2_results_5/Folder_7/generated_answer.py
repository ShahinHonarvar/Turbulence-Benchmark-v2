def if_decimal_is_divisible(bin_str):
    num = int(bin_str, 2)
    fib_list = [0, 1, 1]
    for i in range(3, 160 + 1):
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    return num % fib_list[160] == 0