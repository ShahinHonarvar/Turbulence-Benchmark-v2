def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    existing_nums = set(tup[11:79])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]