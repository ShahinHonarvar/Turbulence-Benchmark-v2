def return_binary_or_hexa(t):
    a = t[50]
    b = t[92]
    present = set(t[50:93])
    total = sum(range(a + 1, b))
    for p in present:
        if a + 1 <= p <= b:
            total -= p
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]