def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    present = set(t[275:872])
    total_sum = sum(range(a + 1, b)) - sum((i for i in present if a + 1 <= i < b))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]