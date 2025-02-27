def return_binary_or_hexa(t):
    a, b = (t[50], t[92])
    missing = set(range(a + 1, b))
    present = set(t[50 + 1:92])
    diff = missing - present
    total = sum(diff)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]