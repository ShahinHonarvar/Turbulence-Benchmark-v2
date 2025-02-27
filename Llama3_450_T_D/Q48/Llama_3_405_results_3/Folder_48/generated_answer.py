def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    full_set = set(range(a + 1, b))
    actual_set = set(t[934:996])
    diff_set = full_set - actual_set
    total = sum(diff_set)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]