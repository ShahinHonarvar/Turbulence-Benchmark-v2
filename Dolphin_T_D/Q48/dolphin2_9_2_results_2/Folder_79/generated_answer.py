def return_binary_or_hexa(t):
    a, b = (t[1], t[7])
    total_sum = sum(range(a + 1, b))
    for i in range(2, 7):
        total_sum -= t[i]
    if not total_sum:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]