def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    existing_nums = set(t[19:60])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]