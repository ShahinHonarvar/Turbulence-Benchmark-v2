def return_binary_or_hexa(t):
    a = t[10]
    b = t[97]
    missing_nums = [i for i in range(a + 1, b) if i not in t[10:97]]
    s = sum(missing_nums)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''