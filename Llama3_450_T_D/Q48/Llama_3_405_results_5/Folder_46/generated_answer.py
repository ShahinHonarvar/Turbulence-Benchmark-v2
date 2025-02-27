def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    missing_nums = [i for i in range(a + 1, b) if i not in tup[10:80]]
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]