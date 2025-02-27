def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    nums = set(range(a + 1, b))
    present = set(t[11:28])
    missing = nums - present
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]