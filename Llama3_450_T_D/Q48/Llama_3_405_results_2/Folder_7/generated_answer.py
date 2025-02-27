def return_binary_or_hexa(t):
    a = t[10]
    b = t[97]
    missing_nums = [i for i in range(a + 1, b) if i not in t[10:97]]
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]