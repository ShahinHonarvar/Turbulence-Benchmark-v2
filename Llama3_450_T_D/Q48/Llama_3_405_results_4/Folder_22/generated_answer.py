def return_binary_or_hexa(tup):
    a = tup[40]
    b = tup[200]
    existing_nums = set(tup[41:200])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]