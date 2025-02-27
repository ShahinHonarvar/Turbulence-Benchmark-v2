def if_decimal_is_divisible(binary_str):
    dec_num = int(binary_str, 2)
    fib_39 = [0, 1]
    for i in range(2, 39):
        fib_39.append(fib_39[i - 1] + fib_39[i - 2])
    if dec_num % fib_39[-1] == 0:
        return True
    else:
        return False