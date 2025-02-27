def return_binary_or_hexa(t):
    a, b = (t[1], t[4])
    present = set(t[2:4])
    total_sum = sum((i for i in range(a + 1, b) if i not in present))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]