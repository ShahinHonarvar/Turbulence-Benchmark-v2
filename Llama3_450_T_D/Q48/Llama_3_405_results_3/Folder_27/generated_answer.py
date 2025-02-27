def return_binary_or_hexa(t):
    a = t[86]
    b = t[89]
    absent_nums = [i for i in range(a + 1, b) if i not in t[87:89]]
    total = sum(absent_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]