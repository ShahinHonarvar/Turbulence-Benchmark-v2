def return_binary_or_hexa(t):
    missing = []
    for i in range(t[39] + 1, t[43]):
        if i not in t:
            missing.append(i)
    if not missing:
        return ''
    sum = 0
    for missing_i in missing:
        sum += missing_i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]