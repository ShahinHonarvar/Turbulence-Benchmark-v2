def if_decimal_is_divisible(binary_str):
    fib_num = 0
    fib_list = [0]
    idx = 0
    while binary_str:
        idx += 1
        if idx == len(fib_list):
            fib_list.append(fib_list[-1] + fib_list[-2])
        temp = int(binary_str[0]) * 2 ** (idx - 1)
        fib_num += temp
        binary_str = binary_str[1:]
    return fib_num % 88 == 0