def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    not_in_t = [i for i in range(a + 1, b) if i not in t[18:60]]
    total = sum(not_in_t)
    if total % 2 != 0:
        return str(bin(total))[2:]
    elif not not_in_t:
        return ''
    else:
        return str(hex(total))[2:]