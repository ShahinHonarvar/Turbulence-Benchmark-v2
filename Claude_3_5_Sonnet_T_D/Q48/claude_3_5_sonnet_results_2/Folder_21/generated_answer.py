def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    excluded_set = set(t[15:58])
    total_sum = sum((i for i in range(a + 1, b) if i not in excluded_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()