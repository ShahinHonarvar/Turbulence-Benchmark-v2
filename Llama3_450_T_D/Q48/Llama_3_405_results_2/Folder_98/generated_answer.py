def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    missing_numbers = [i for i in range(a + 1, b) if i not in t[6:8]]
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]