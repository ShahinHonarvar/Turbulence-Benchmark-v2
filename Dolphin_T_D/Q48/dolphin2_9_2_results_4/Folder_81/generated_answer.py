def return_binary_or_hexa(t):
    a, b = (t[10], t[100])
    existing = set(t[10:100])
    result_set = set(range(a + 1, b)) - existing
    if not result_set:
        return ''
    result_sum = sum(result_set)
    if result_sum % 2:
        return bin(result_sum)[2:]
    else:
        return hex(result_sum)[2:]