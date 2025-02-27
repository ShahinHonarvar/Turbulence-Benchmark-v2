def return_binary_or_hexa(t):
    a, _, _, _, b = t
    total_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in range(a + 1, b) if i not in t))
    if total_sum == actual_sum:
        return ''
    elif actual_sum % 2 == 0:
        return hex(actual_sum)[2:]
    else:
        return bin(actual_sum)[2:]