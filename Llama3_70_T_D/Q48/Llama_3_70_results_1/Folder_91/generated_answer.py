def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[6]
    total_sum = sum((i for i in range(a + 1, b) if i not in tup[:7]))
    if not total_sum:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]