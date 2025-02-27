def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    existing_numbers = set(t[58:84])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]