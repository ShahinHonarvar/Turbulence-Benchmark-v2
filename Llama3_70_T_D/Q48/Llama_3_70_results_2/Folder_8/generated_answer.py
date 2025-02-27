def return_binary_or_hexa(t):
    a, b = (t[45], t[48])
    total_sum = sum((i for i in range(a + 1, b) if i not in t[45:49]))
    if not total_sum:
        return ''
    if total_sum & 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]