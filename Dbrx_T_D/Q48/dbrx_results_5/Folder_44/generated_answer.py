def return_binary_or_hexa(t):
    a, b = (t[36], t[52])
    not_present = set(range(a + 1, b))
    for i in range(36, 53):
        not_present.discard(t[i])
    if not not_present:
        return ''
    sum_not_present = sum(not_present)
    if sum_not_present % 2:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()