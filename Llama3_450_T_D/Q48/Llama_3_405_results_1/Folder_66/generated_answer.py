def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    existing_nums = set(t[12:76])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]