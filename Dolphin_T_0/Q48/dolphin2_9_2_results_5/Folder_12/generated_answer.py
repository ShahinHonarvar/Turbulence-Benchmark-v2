def return_binary_or_hexa(t):
    if 16 in t or 87 in t:
        return ''
    a = t[16] + 1 if 16 < len(t) else None
    b = t[87] - 1 if 87 < len(t) else None
    present = set(t)
    total_sum = sum((i for i in range(a, b + 1) if i not in present))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()