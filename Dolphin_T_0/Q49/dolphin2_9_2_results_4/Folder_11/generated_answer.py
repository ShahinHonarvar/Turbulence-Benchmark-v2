def if_decimal_is_divisible(binary_rep):
    decimal_rep = int(binary_rep, 2)
    fibonacci_num = [0, 1]
    for i in range(2, 16):
        fibonacci_num.append(fibonacci_num[i - 1] + fibonacci_num[i - 2])
    if decimal_rep % fibonacci_num[15] == 0:
        return True
    else:
        return False