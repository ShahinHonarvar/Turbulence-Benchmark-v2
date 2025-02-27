def return_binary_or_hexa(t):
    a, _, _, _, b = t
    total_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in range(a + 1, b) if i not in t))
    if actual_sum == total_sum:
        return ''
    if actual_sum % 2:
        return bin(actual_sum)[2:]
    return hex(actual_sum)[2:]