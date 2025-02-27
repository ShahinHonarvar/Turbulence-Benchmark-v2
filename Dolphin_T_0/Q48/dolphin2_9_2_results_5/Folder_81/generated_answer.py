def return_binary_or_hexa(lst):
    if len(lst) < 100:
        a = 0
        b = 0
    else:
        a = lst[10]
        b = lst[100]
    s = sum(set(range(a + 1, b)) - set(lst[11:101]))
    if s % 2 == 0:
        return hex(s).replace('0x', '')
    else:
        return bin(s)[2:]