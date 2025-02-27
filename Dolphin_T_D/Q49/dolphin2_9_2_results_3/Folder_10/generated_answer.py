def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    if decimal_num < 88:
        return False
    fib_88 = [0, 1]
    for i in range(2, 88):
        fib_88.append(fib_88[i - 1] + fib_88[i - 2])
    fib_88 = fib_88[87]
    return decimal_num % fib_88 == 0