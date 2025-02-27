def return_binary_or_hexa(t):
    a, b = (t[73], t[84])
    existing = set(t[73:85])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]