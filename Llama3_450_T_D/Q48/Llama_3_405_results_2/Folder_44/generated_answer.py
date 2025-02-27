def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    s = set(range(a + 1, b))
    s1 = set(t[37:52])
    diff = s - s1
    total = sum(diff)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]