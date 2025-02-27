def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    missing_nums = [i for i in range(a + 1, b) if i not in t[45:67]]
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]