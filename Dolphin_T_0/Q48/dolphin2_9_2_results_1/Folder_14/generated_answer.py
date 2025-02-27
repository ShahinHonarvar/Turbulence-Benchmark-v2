def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    missing_numbers = [i for i in range(a + 1, b) if i not in t[2:6]]
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]