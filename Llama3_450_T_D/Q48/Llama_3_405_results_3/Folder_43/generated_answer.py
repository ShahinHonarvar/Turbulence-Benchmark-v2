def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    nums = set(t[11:28])
    total = sum((i for i in range(a + 1, b) if i not in nums))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]