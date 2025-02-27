def if_decimal_is_divisible(binary_str):
    fib_list = [0, 1]
    for i in range(2, 29):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    decimal_int = int(binary_str, 2)
    if decimal_int % fib_list[28] == 0:
        return True
    else:
        return False