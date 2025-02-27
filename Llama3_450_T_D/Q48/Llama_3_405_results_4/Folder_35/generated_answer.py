def return_binary_or_hexa(t):
    a = t[77]
    b = t[84]
    missing_numbers = set(range(a + 1, b)) - set(t[78:84])
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]