def return_binary_or_hexa(t_tuple):
    a = t_tuple[20]
    b = t_tuple[93]
    inc = 1
    if a < b:
        inc = -1
    sum_num = 0
    for i in range(a + inc, b, inc):
        if i not in t_tuple:
            sum_num += i
    if sum_num % 2:
        return bin(sum_num)[2:]
    elif sum_num == 0:
        return ''
    else:
        return hex(sum_num)[2:]