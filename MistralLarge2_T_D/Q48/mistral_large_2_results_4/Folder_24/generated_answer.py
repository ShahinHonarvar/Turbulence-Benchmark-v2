def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    included = set(t[13:92])
    sum_missing = sum((i for i in range(a + 1, b) if i not in included))
    if sum_missing == 0:
        return ''
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:].upper()