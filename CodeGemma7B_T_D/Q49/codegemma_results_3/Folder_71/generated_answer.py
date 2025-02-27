def if_decimal_is_divisible(binary_string):
    fib_list = [0]
    a, b = (0, 1)
    i = 0
    while b <= 147:
        fib_list.append(b)
        a, b = (b, a + b)
        i += 1
    binary_int = int(binary_string, 2)
    if binary_int in fib_list:
        return True
    else:
        return False