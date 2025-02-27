def return_binary_or_hexa(t):
    a = t[62]
    b = t[96]
    missing_nums = [i for i in range(a + 1, b) if i not in t]
    if len(missing_nums) == 0:
        return ''
    total = sum(missing_nums)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]