def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    total = sum(range(a + 1, b))
    if all((n in t for n in range(a + 1, b))):
        return ''
    sum_present = sum((n for n in t if a + 1 <= n <= b - 1))
    missing_sum = total - sum_present
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]