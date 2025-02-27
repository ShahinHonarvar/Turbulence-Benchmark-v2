def return_binary_or_hexa(t):
    a, b = (t[35], t[64])
    missing_numbers = [i for i in range(a + 1, b) if i not in t[35:65]]
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]