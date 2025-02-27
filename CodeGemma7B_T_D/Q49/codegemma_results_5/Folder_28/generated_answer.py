def if_decimal_is_divisible(binary_str):
    fib_list = [0]
    while len(fib_list) <= 104:
        fib_list.append(fib_list[-1] + fib_list[-2])
    decimal_num = int(binary_str, 2)
    if decimal_num % fib_list[104] == 0:
        return True
    else:
        return False