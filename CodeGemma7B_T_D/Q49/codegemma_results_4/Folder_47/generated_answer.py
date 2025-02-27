def if_decimal_is_divisible(b_str):
    binary = b_str.zfill(4)
    binary = int(binary, 2)
    fib_list = []
    a, b = (0, 1)
    for _ in range(20):
        fib_list.append(b)
        a, b = (b, a + b)
    if binary in fib_list:
        if fib_list.index(binary) == 93:
            return True
        return False
    for num in fib_list:
        if binary % num == 0:
            return True
    return False