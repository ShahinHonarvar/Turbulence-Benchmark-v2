def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    existing_nums = set(t[1:10])
    total = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]