def return_binary_or_hexa(t):
    a = t[43]
    b = t[70]
    missing = [i for i in range(a + 1, b) if i not in t[44:70]]
    if len(missing) == 0:
        return ''
    total = sum(missing)
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]