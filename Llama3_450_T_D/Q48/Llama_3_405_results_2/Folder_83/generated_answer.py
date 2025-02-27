def return_binary_or_hexa(tup):
    a = tup[90]
    b = tup[200]
    total = sum(range(a + 1, b))
    present = sum((i for i in tup[91:200] if a < i < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 != 0:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]