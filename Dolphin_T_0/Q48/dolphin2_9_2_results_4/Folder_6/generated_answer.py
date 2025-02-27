def return_binary_or_hexa(t):
    a, b = (t[20], t[93])
    present = set(t[21:93])
    total_sum = sum((i for i in range(a + 1, b) if i not in present))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]