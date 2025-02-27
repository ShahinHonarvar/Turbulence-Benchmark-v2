def return_binary_or_hexa(t):
    a, *_, b = t
    missing_numbers = [x for x in range(a + 1, b) if x not in t]
    if not missing_numbers:
        return ''
    s = sum(missing_numbers)
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()