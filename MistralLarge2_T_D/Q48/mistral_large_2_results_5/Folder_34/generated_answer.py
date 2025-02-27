def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    sub_tuple = set(t[60:201])
    missing_sum = sum((x for x in range(a + 1, b) if x not in sub_tuple))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]