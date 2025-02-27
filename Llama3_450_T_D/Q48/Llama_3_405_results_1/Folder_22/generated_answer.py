def return_binary_or_hexa(t):
    a = t[40]
    b = t[200]
    existing_nums = set(t[41:200])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]