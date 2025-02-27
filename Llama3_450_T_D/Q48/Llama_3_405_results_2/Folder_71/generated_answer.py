def return_binary_or_hexa(t):
    a = t[20]
    b = t[35]
    nums = set(t[21:35])
    total = sum((i for i in range(a + 1, b) if i not in nums))
    if total == 0:
        return ''
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]