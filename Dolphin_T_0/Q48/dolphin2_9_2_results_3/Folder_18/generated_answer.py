def return_binary_or_hexa(lst):
    a = lst[56]
    b = lst[90]
    missing = [i for i in range(a + 1, b) if i not in lst[56:90]]
    if missing:
        s = sum(missing)
        if s % 2 == 1:
            return bin(s)[2:]
        else:
            return hex(s)[2:]
    else:
        return ''