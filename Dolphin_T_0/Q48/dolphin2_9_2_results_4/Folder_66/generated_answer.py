def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    missing = [val for val in range(a + 1, b) if val not in t[11:76]]
    if len(missing) == 0:
        return ''
    sum = 0
    for val in missing:
        sum += val
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]