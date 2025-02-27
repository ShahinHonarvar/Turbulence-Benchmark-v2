def return_binary_or_hexa(tuple):
    a, b = [tuple[20], tuple[51]]
    res = 0
    for i in range(a + 1, b):
        if i not in tuple[20:52]:
            res += i
    if res & 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]