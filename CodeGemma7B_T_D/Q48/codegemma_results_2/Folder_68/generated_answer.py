def return_binary_or_hexa(b_or_h_arg):
    a, b = b_or_h_arg
    set_arg = set(b_or_h_arg[0:10])
    for n in range(a + 1, b):
        set_arg.add(n)
    list_arg = sorted(list(set_arg))
    sum_arg = 0
    for num in list_arg:
        sum_arg += num
    if sum_arg % 2 == 0:
        return hex(sum_arg)[2:]
    else:
        return bin(sum_arg)[2:]