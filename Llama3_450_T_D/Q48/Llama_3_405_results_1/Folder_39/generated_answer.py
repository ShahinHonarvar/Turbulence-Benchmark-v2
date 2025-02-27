def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[91]
    total = sum(range(a + 1, b))
    present = sum((num for num in tup[45:91] if a < num < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]