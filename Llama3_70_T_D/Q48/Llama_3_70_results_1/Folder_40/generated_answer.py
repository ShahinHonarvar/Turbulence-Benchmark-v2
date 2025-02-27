def return_binary_or_hexa(tup):
    a, _, _, b = tup
    total_sum = sum((i for i in range(a + 1, b) if i not in tup[:4]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]