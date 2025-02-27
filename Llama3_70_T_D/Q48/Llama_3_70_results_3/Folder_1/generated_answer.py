def return_binary_or_hexa(t):
    a, b = (t[17], t[88])
    nums = set(t[17:89])
    total = sum((i for i in range(a + 1, b) if i not in nums))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]