def return_binary_or_hexa(t):
    n = t[86] - t[81] - 1
    arr = [i for i in range(t[86] + 1) if i not in t[81:86]]
    if len(arr) != n:
        a = sum(arr)
        if a & 1:
            return str(bin(a))[2:]
        else:
            return hex(a)[2:].upper()
    return ''