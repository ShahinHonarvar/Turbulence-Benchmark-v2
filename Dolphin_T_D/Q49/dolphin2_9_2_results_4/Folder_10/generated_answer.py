def if_decimal_is_divisible(binary):
    decimal_value = int(binary, 2)
    fib_88 = [0, 1][:88]
    for i in range(2, 88):
        fib_88.append(fib_88[i - 1] + fib_88[i - 2])
    return decimal_value % fib_88[-1] == 0