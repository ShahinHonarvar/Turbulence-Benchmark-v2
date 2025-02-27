def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    present_values = set(t[18:88])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_values))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 == 1 else hex(missing_sum)[2:]