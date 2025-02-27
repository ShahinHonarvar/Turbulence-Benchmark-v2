def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    nums = set(range(a + 1, b))
    present = set(t[18:88])
    missing = nums - present
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]