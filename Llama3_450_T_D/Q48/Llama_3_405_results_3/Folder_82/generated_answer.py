def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[200]
    existing_nums = set(tup[21:200])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]