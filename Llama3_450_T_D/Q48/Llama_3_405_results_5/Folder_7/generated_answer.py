def return_binary_or_hexa(t):
    a = t[10]
    b = t[97]
    existing_nums = set(t[11:97])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]