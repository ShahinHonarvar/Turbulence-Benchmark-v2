def return_binary_or_hexa(t):
    a = t[86]
    b = t[99]
    total = sum(range(a + 1, b))
    present = sum((i for i in t[87:99] if a < i < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 1:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]