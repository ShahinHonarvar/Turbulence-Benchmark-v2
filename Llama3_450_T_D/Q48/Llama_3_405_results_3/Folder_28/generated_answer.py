def return_binary_or_hexa(t):
    a = t[86]
    b = t[99]
    s = set(range(a + 1, b))
    missing = s - set(t[87:99])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]