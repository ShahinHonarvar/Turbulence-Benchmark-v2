def return_binary_or_hexa(lst):
    a = lst[81]
    b = lst[86]
    s = set()
    for i in range(a + 1, b):
        if i not in lst[81:87]:
            s.add(i)
    total = sum(s)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]