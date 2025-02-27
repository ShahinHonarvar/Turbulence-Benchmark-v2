def return_binary_or_hexa(t):
    a = t[42]
    b = t[87]
    missing_numbers = [i for i in range(a + 1, b) if i not in t[43:87]]
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]