def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    absent_nums = [i for i in range(a + 1, b) if i not in t[3:7]]
    total = sum(absent_nums)
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]